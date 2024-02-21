from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import bid_service, localization_service
from ..models import Property, Bid


def place_bid(request, property_id: int):
    prop = get_object_or_404(Property, pk=property_id)  # Retrieve the property instance
    try:
        bid_value = int(request.POST['bid'])
        valid, err = bid_service.bid_is_valid(prop, bid_value)
        if valid:
            bid_instance = Bid(property=prop, bid=bid_value, user=request.user)
            bid_instance.save()
            return HttpResponseRedirect(reverse('bidder:detail', args=(prop.id,)))

        context = fetch_property_context(
            request, property_id, err
        )
        context["input_bid"] = bid_value
        return render(request, 'bidder/detail.html', context)
    except (KeyError, ValueError):
        # Return the form with an error message if something goes wrong (e.g., bid is not a number)
        context = fetch_property_context(
            request, property_id, "Invalid bid. Please enter a valid number"
        )
        return render(request, 'bidder/detail.html', context)


def fetch_property_list_context(request):
    # Start with an empty query
    properties_query = Q()

    # If there's a search query, filter properties by the search term
    query = request.GET.get('query', '')
    if query:
        properties_query &= Q(address__icontains=query)

    # If the user is staff, they can see all properties, otherwise, filter by viewable properties
    if not request.user.is_staff:
        properties_query &= Q(viewable_by_users__id=request.user.id)

    # Execute the query
    latest_property_list = Property.objects.filter(properties_query).distinct().order_by("address")

    return {
        "latest_property_list": latest_property_list,
        "query": query
    }


def fetch_property_context(request, property_id, error_message=None):
    prop = get_object_or_404(Property, pk=property_id)
    top_bid = bid_service.get_top_bid(property_id)
    user_bid = bid_service.get_top_bid_for_user(property_id, request.user.id)

    top_bid_text = localization_service.format_number_as_pound_value_commas(top_bid)
    if top_bid == 0:
        top_bid_text = "No bids have been placed yet on this property"

    # Initialize context with data available to all users
    context = {
        "property": prop,
        "top_bid": top_bid_text,
        "user_bid": localization_service.format_number_as_pound_value_commas(user_bid),
        "minimum_increment": localization_service.format_number_as_pound_value_commas(prop.minimum_increment),
        "bids_list": None  # Default to None for non-staff users
    }

    # Add error message to context if present
    if error_message:
        context["error_message"] = error_message

    # Check if user has the 'view_bids' permission, you can create custom permissions for your models
    if request.user.is_staff:
        context['bids_list'] = bid_service.get_all_bids(property_id)

    return context


def can_view_property(user, property_id):
    return user.is_staff or user.viewable_properties.filter(id=property_id).exists()
