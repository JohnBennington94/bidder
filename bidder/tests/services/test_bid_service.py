# pylint: disable=redefined-outer-name
from unittest.mock import patch

import pytest

from ...services.bid_service import Property, bid_is_valid


@pytest.fixture
def mock_bid_service():
    with patch('bidder.services.bid_service.get_top_bid') as mock_get_top_bid, \
         patch('bidder.services.bid_service.get_top_bid_for_user') as mock_get_top_bid_for_user:
        # Set return values or side effects for your mocks here
        mock_get_top_bid.return_value = 0
        mock_get_top_bid_for_user.return_value = 0
        yield mock_get_top_bid, mock_get_top_bid_for_user


def test_bid_less_than_top_bid_is_not_valid(mock_bid_service):
    mock_get_top_bid, mock_get_top_bid_for_user = mock_bid_service

    # Set return values for this specific test
    mock_get_top_bid.return_value = 150
    mock_get_top_bid_for_user.return_value = 70

    prop = Property(address='123 Test St', minimum_increment=1)
    valid, err = bid_is_valid(prop, 149)
    assert not valid
    assert err == "Bid does not exceed the current maximum bid"


def test_bid_more_than_top_bid_is_valid(mock_bid_service):
    mock_get_top_bid, mock_get_top_bid_for_user = mock_bid_service

    # Set return values for this specific test
    mock_get_top_bid.return_value = 150
    mock_get_top_bid_for_user.return_value = 70

    prop = Property(address='123 Test St', minimum_increment=1)
    assert bid_is_valid(prop, 151)
    valid, err = bid_is_valid(prop, 151)
    assert valid
    assert err == ""


def test_bid_increase_less_than_minimum_increment_is_not_valid(mock_bid_service):
    mock_get_top_bid, mock_get_top_bid_for_user = mock_bid_service

    # Set return values for this specific test
    mock_get_top_bid.return_value = 150
    mock_get_top_bid_for_user.return_value = 70

    prop = Property(address='123 Test St', minimum_increment=50)
    valid, err = bid_is_valid(prop, 199)
    assert not valid
    assert err == "Bid does not exceed the minimum increment"


def test_bid_increase_equal_to_minimum_increment_is_valid(mock_bid_service):
    mock_get_top_bid, mock_get_top_bid_for_user = mock_bid_service

    # Set return values for this specific test
    mock_get_top_bid.return_value = 150
    mock_get_top_bid_for_user.return_value = 70

    prop = Property(address='123 Test St', minimum_increment=50)
    valid, err = bid_is_valid(prop, 200)
    assert valid
    assert err == ""
