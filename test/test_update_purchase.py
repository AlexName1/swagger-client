# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.update_purchase import UpdatePurchase


class TestUpdatePurchase(unittest.TestCase):
    """UpdatePurchase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdatePurchase:
        """Test UpdatePurchase
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UpdatePurchase`
        """
        model = UpdatePurchase()
        if include_optional:
            return UpdatePurchase(
                purchase_id = 56,
                add_info = '',
                add_photo = '',
                status = 56
            )
        else:
            return UpdatePurchase(
                purchase_id = 56,
        )
        """

    def testUpdatePurchase(self):
        """Test UpdatePurchase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
