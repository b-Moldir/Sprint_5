from helpers import create_courier_payload
from data import PAYLOAD, INCORRECT_LOGIN, INCORRECT_PASSWORD, PAYLOAD_ONLY_PASSWORD


class TestAuthorizeCourier:

    def test_authorize_courier(self, courier_methods):
        payload = courier_methods.register_new_courier_and_return_login_password()
        status_code, response_json = courier_methods.authorize_courier(payload)
        assert status_code == 200 and response_json

    def test_enter_wrong_login_response_error(self, courier_methods):
        courier_methods.create_courier(PAYLOAD)
        status_code, response_json = courier_methods.authorize_courier(INCORRECT_LOGIN)
        assert status_code == 404 and response_json

    def test_enter_wrong_password_response_error(self, courier_methods):
        courier_methods.create_courier(PAYLOAD)
        status_code, response_json = courier_methods.authorize_courier(INCORRECT_PASSWORD)
        assert status_code == 404 and response_json

    def test_missing_field_response_error(self, courier_methods):
        courier_methods.create_courier(PAYLOAD_ONLY_PASSWORD)
        status_code, response_json = courier_methods.authorize_courier(PAYLOAD_ONLY_PASSWORD)
        assert status_code == 400 and response_json

    def test_authorize_nonexistent_courier(self, courier_methods):
        courier_methods.create_courier(PAYLOAD)
        status_code, response_json = courier_methods.authorize_courier(INCORRECT_LOGIN)
        assert status_code == 404 and response_json

    def test_successfull_response_id(self, courier_methods):
        payload = create_courier_payload()
        courier_methods.create_courier(payload)
        _, response_json = courier_methods.authorize_courier(payload)
        assert 'id' in response_json




