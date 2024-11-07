from data import BODY_DATA_1

class TestGetOrderByNumber:
    def test_successful_response_object_with_order(self, orders_methods):
        response = orders_methods.post_orders(BODY_DATA_1)
        response_json = response[1]
        order_id = response_json.get('track')
        status_code, response_json = orders_methods.get_order_by_number(order_id)
        assert status_code == 200 and response_json

    def test_without_courier_id_response_error(self, orders_methods):
        status_code, response_json = orders_methods.get_order_by_number('')
        assert status_code == 400 and response_json

    def test_incorrect_order_id_response_error(self, orders_methods):
        order_id = 123456
        status_code, response_json = orders_methods.get_order_by_number(order_id)
        assert status_code == 404 and response_json