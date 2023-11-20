# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.api.orders_api import OrdersApi


class TestOrdersApi(unittest.TestCase):
    """OrdersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrdersApi()

    def tearDown(self) -> None:
        pass

    def test_delete_order_api_v1_orders_order_id_delete(self) -> None:
        """Test case for delete_order_api_v1_orders_order_id_delete

        Delete Order
        """
        pass

    def test_get_active_orders_api_v1_orders_get(self) -> None:
        """Test case for get_active_orders_api_v1_orders_get

        Get Active Orders
        """
        pass

    def test_get_count_orders_api_v1_orders_count_get(self) -> None:
        """Test case for get_count_orders_api_v1_orders_count_get

        Get Count Orders
        """
        pass

    def test_get_count_orders_by_user_id_api_v1_orders_users_user_id_count_get(self) -> None:
        """Test case for get_count_orders_by_user_id_api_v1_orders_users_user_id_count_get

        Get Count Orders By User Id
        """
        pass

    def test_get_order_by_id_api_v1_orders_order_id_get(self) -> None:
        """Test case for get_order_by_id_api_v1_orders_order_id_get

        Get Order By Id
        """
        pass

    def test_get_user_orders_api_v1_orders_users_user_id_get(self) -> None:
        """Test case for get_user_orders_api_v1_orders_users_user_id_get

        Get User Orders
        """
        pass

    def test_insert_order_api_v1_orders_post(self) -> None:
        """Test case for insert_order_api_v1_orders_post

        Insert Order
        """
        pass


if __name__ == '__main__':
    unittest.main()
