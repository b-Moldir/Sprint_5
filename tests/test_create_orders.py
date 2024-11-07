import pytest
from data import BODY_DATA_1, BODY_DATA_2,BODY_DATA_3,BODY_DATA_4

class TestCreateOrders:
    @pytest.mark.parametrize('body', [BODY_DATA_1, BODY_DATA_2, BODY_DATA_3, BODY_DATA_4])
    def test_create_order_with_or_no_color(self, orders_methods,body):
        status_code, response_json = orders_methods.post_orders(body)
        assert status_code == 201 and 'track' in response_json


