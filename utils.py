import json
import random

import requests


class Utils:
    URL_AUTH = "https://restful-booker.herokuapp.com/auth"
    URL_BOOKING = "https://restful-booker.herokuapp.com/booking"

    CREDENTIALS = json.dumps({
        "username": "admin",
        "password": "password123"
    })

    HEADERS = {
        'Content-Type': 'application/json'
    }

    HEADERS_TOKEN = {
        'Content-Type': 'application/json'
    }

    def get_token(self):
        response = requests.post(self.URL_AUTH, headers=self.HEADERS, data=self.CREDENTIALS)
        return response.json()["token"]

    def get_random_bookingid(self):
        response = requests.get(self.URL_BOOKING)
        random_booking = random.choice(response.json())
        return random_booking["bookingid"]

    def get_headers_and_token(self, token):
        self.HEADERS_TOKEN['Cookie'] = token
        return self.HEADERS_TOKEN

    def get_url_random_booking(self):
        return self.URL_BOOKING + "/" + str(self.get_random_bookingid())

