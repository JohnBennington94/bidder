from ..models import Property, Bid


def bid_is_valid(prop: Property, bid_value: int):
    error_message = ""
    if not bid_exceeds_top_bid(prop.id, bid_value):
        error_message = "Bid does not exceed the current maximum bid"
        return False, error_message
    if not bid_increment_exceeds_minimum(prop, bid_value):
        error_message = "Bid does not exceed the minimum increment"
        return False, error_message
    return True, error_message


def bid_increment_exceeds_minimum(prop: Property, bid_value: int):
    """Check that bid exceeds the minimum increment value"""
    return (bid_value - get_top_bid(prop.id)) >= prop.minimum_increment


def bid_exceeds_top_bid(prop_id: int, bid_value: int):
    """Check that bid exceeds the current top bid for a property"""
    return bid_value > get_top_bid(prop_id)


def get_top_bid(property_id: int):
    """Get the top bid for a particular property"""
    bid_object = Bid.objects.filter(property_id=property_id).order_by('-bid').first()
    return bid_object.bid if bid_object else 0


def get_top_bid_for_user(prop_id: int, user_id: int):
    """Get the top bid by a particular user for a particular property"""
    bid_object = Bid.objects.filter(property_id=prop_id, user_id=user_id).order_by('-bid').first()
    return bid_object.bid if bid_object else 0


def get_all_bids(property_id: int):
    """Get all the bids for a particular property"""
    return Bid.objects.filter(property_id=property_id).order_by('-bid')
