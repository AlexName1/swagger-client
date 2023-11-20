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

from swagger_client.models.yookassa_payment_base import YookassaPaymentBase

class TestYookassaPaymentBase(unittest.TestCase):
    """YookassaPaymentBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> YookassaPaymentBase:
        """Test YookassaPaymentBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `YookassaPaymentBase`
        """
        model = YookassaPaymentBase()
        if include_optional:
            return YookassaPaymentBase(
                id = 56,
                purchase_id = 56,
                payment_id = '',
                status = '',
                captured_at = '',
                email = ''
            )
        else:
            return YookassaPaymentBase(
        )
        """

    def testYookassaPaymentBase(self):
        """Test YookassaPaymentBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
