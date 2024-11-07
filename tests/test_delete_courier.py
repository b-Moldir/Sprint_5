from helpers import create_courier_payload


class TestDeleteCourier:
    def test_unsuccessful_request_return_error(self, courier_methods):
        status_code, response_json = courier_methods.delete_courier(5)
        assert status_code == 404 and response_json

    def test_successful_response(self, courier_methods):
        payload = create_courier_payload()
        courier_methods.create_courier(payload)
        response_json = courier_methods.authorize_courier(payload)
        response = response_json[1]
        courier_id = response.get('id')
        response_delete = courier_methods.delete_courier(courier_id)
        response_json_delete = response_delete[1]
        assert "ok" in response_json_delete and response_json_delete["ok"]
