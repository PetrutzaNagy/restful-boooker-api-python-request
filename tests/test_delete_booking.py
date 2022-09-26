import pytest
import requests
from assertpy import assert_that

from utils import Utils


@pytest.fixture
def utils():
    return Utils()


def test_delete_random_booking(utils):
    url_booking = utils.get_url_random_booking()
    response = requests.request("DELETE", url_booking, headers=utils.get_headers_and_token("token="+utils.get_token()))
    assert_that(response.status_code).is_equal_to(201)
    response = requests.request("GET", url_booking)
    assert_that(response.status_code).is_equal_to(404)


def test_delete_without_token(utils):
    response = requests.request("DELETE", utils.get_url_random_booking(), headers=utils.HEADERS)
    assert_that(response.status_code).is_equal_to(403)
