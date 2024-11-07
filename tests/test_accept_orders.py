from data import BODY_DATA_1



class TestAcceptOrders:
    def test_successful_response(self, courier_methods, orders_methods):
        payload = courier_methods.register_new_courier_and_return_login_password()
        response_json = courier_methods.authorize_courier(payload)
        response = response_json[1]
        courier_id = response.get('id')
        response_json2 = orders_methods.post_orders(BODY_DATA_1)
        response2 = response_json2[1]
        order_id = response2.get('track')
        response_accept = orders_methods.accept_order(order_id, courier_id)
        response_json_accept = response_accept[1]
        assert "ok" in response_json_accept and response_json_accept["ok"]

    def test_without_courier_id_response_error(self, courier_methods, orders_methods):
        response_json2 = orders_methods.post_orders(BODY_DATA_1)
        response2 = response_json2[1]
        order_id = response2.get('track')
        status_code, response_json = orders_methods.accept_order(order_id, '')
        assert status_code == 400 and response_json

    def test_incorrect_courier_id_response_error(self, courier_methods, orders_methods):
        courier_id = 213
        response_json2 = orders_methods.post_orders(BODY_DATA_1)
        response2 = response_json2[1]
        order_id = response2.get('track')
        status_code, response_json = orders_methods.accept_order(order_id, courier_id)
        assert status_code == 404 and response_json

    def test_without_order_id_response_error(self, courier_methods, orders_methods):
        payload = courier_methods.register_new_courier_and_return_login_password()
        response_json = courier_methods.authorize_courier(payload)
        response = response_json[1]
        courier_id = response.get('id')
        status_code, response_json = orders_methods.accept_order('', courier_id)
        assert status_code == 404 and response_json

    def test_incorrect_order_id_response_error(self, courier_methods, orders_methods):
        payload = courier_methods.register_new_courier_and_return_login_password()
        response_json = courier_methods.authorize_courier(payload)
        response = response_json[1]
        courier_id = response.get('id')
        order_id = 954574
        status_code, response_json = orders_methods.accept_order(order_id, courier_id)
        assert status_code == 404 and response_json