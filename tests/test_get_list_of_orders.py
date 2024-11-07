from data import BODY_DATA_1


class TestGetListOrders:
    def test_get_list_of_orders(self, orders_methods):
        orders_methods.post_orders(BODY_DATA_1)
        status_code, response_json = orders_methods.get_list_of_orders()
        assert status_code == 200 and response_json