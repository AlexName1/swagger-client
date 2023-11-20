# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from swagger_client.models.stock_base import StockBase

class TestStockBase(unittest.TestCase):
    """StockBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StockBase:
        """Test StockBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StockBase`
        """
        model = StockBase()
        if include_optional:
            return StockBase(
                id = '',
                name = '',
                user_id = 56,
                number = 56,
                shipment_point = ''
            )
        else:
            return StockBase(
        )
        """

    def testStockBase(self):
        """Test StockBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
