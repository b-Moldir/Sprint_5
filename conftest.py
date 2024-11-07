import pytest

from methods.courier_methods import CourierMethods
from methods.orders_methods import OrdersMethods


@pytest.fixture()
def courier_methods():
    return CourierMethods()


@pytest.fixture()
def orders_methods():
    return OrdersMethods()


@pytest.fixture()
def courier(courier_methods, payload=None):
    response = courier_methods.create_courier(payload)
    yield response.json()['id']
    courier_methods.delete_courier(response.json()['id'])
