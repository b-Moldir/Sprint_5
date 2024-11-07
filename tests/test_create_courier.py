from helpers import create_courier_payload


class TestCreateCourier:

    def test_create_courier(self,courier_methods):
        payload = create_courier_payload()
        status_code, response_json = courier_methods.create_courier(payload)
        assert status_code == 201 and response_json

    def test_duplicate_courier(self,courier_methods):
        payload = create_courier_payload()
        status_code, response_json = courier_methods.create_courier(payload)
        assert status_code == 201 and response_json

        status_code, response_json = courier_methods.create_courier(payload)
        assert status_code == 409 and response_json

    def test_correct_response_code(self, courier_methods):
        payload = create_courier_payload()
        status_code, _ = courier_methods.create_courier(payload)
        assert status_code == 201

    def test_successful_response(self,courier_methods):
        payload = create_courier_payload()
        _, response_json = courier_methods.create_courier(payload)
        assert "ok" in response_json and response_json["ok"] is True

    def test_crate_courier_missing_fields(self,courier_methods):
        payload = {
            "password": 1234,
            "firstName": "saske"
        }
        status_code, response_json = courier_methods.create_courier(payload)
        assert status_code == 400 and response_json

