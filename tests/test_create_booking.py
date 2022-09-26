import requests
from assertpy import assert_that, soft_assertions
import json
from utils import Utils


def test_create_booking():
    utils = Utils()
    token = utils.get_token()
    details = json.dumps({
        "firstname": "test",
        "lastname": "testrrt",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    })

    # response = requests.post("https://restful-booker.herokuapp.com/booking", headers = headers, data = details)
    response = requests.request("POST", utils.URL_BOOKING, headers=utils.get_headers_and_token(utils.get_token()), data=details)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()["booking"]["firstname"]).is_equal_to("test")
    assert_that(response.json()["booking"]["lastname"]).is_equal_to("testrrt")
    assert_that(response.json()["booking"]["totalprice"]).is_equal_to(111)
    booking_id = response.json()["bookingid"]
    response = requests.get("https://restful-booker.herokuapp.com/booking/" + str(booking_id))
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()["firstname"]).is_equal_to("test")
        assert_that(response.json()["lastname"]).is_equal_to("testrrt")
        assert_that(response.json()["depositpaid"]).is_true()
