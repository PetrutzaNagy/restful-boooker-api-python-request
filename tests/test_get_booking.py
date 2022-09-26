import pytest
import requests
from assertpy import assert_that
from assertpy import soft_assertions

from utils import Utils


@pytest.fixture
def utils():
    return Utils()


def test_get_all_bookings(utils):
    response = requests.get(utils.URL_BOOKING)
    with soft_assertions():
        assert_that(response.status_code, "Response is not ok").is_equal_to(200)
        assert_that(len(response.json())).is_greater_than(10)
        for i in range(len(response.json())):
            assert_that(response.json()[i]["bookingid"], "Booking id is missing").is_not_none()


def test_get_one_booking(utils):
    response = requests.get(utils.get_url_random_booking())
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).contains_key("firstname")
        assert_that(response.json()).contains_key("lastname")
        assert_that(response.json()).contains_key("depositpaid")
        assert_that(response.json()).contains_key("totalprice")
        assert_that(response.json()).contains_key("bookingdates")
