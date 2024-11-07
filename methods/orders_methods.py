import requests
from data import BASE_URL, ORDERS_URL, ACCEPT_URL, TRACK_URL

class OrdersMethods:

    def post_orders(self, body):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=body)
        return response.status_code, response.json()

    def get_list_of_orders(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response.status_code, response.json()

    def accept_order(self, order_id, courier_id):
        response = requests.put(f'{BASE_URL}{ORDERS_URL}{ACCEPT_URL}{order_id}?courierId={courier_id}')
        return response.status_code, response.json()

    def accept_order_without_order_id(self, courier_id):
        response = requests.put(f'{BASE_URL}{ORDERS_URL}{ACCEPT_URL}{courier_id}')
        return response.status_code, response.json()


    def get_order_by_number(self, order_id):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}{TRACK_URL}?t={order_id}')
        return response.status_code, response.json()

