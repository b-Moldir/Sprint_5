import requests
from data import BASE_URL,COURIER_URL
from helpers import create_courier_payload


class CourierMethods:

    def register_new_courier_and_return_login_password(self):
        payload = create_courier_payload()
        response = requests.post(f'{BASE_URL}{COURIER_URL}', json=payload)
        if response.status_code == 201:
            return payload

    def create_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIER_URL}', json=payload)
        return response.status_code, response.json()

    def authorize_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIER_URL}{'login'}',json=payload )
        return response.status_code, response.json()

    def delete_courier(self, courier_id):
        response = requests.delete(f'{BASE_URL}/courier/{courier_id}')
        return response.status_code, response.json()

