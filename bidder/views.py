from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .services import property_service
from .forms import MyLoginForm


def user_login(request):
    if request.method == 'POST':
        form = MyLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('bidder:index')  # Redirect to a success page.
    else:
        form = MyLoginForm()
    return render(request, 'bidder/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('bidder:login')  # Redirect to the index page after logout


@login_required
def index(request):
    context = property_service.fetch_property_list_context(request)
    return render(request, "bidder/index.html", context)


@login_required
def detail(request, property_id):
    if property_service.can_view_property(request.user, property_id):
        context = property_service.fetch_property_context(request, property_id, None)
        return render(request, "bidder/detail.html", context)
    return index(request)


@login_required
def bid(request, property_id):
    if property_service.can_view_property(request.user, property_id):
        return property_service.place_bid(request, property_id)
    return index(request)


@login_required
def help_view(request):
    return render(request, "bidder/help.html")


@login_required
def user_details(request):
    return render(request, "bidder/user.html")
