# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.update_info_item_new import UpdateInfoItemNew

class TestUpdateInfoItemNew(unittest.TestCase):
    """UpdateInfoItemNew unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateInfoItemNew:
        """Test UpdateInfoItemNew
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateInfoItemNew`
        """
        model = UpdateInfoItemNew()
        if include_optional:
            return UpdateInfoItemNew(
                code = '',
                retail_price = 56,
                link = '',
                discount_price = 56
            )
        else:
            return UpdateInfoItemNew(
                code = '',
        )
        """

    def testUpdateInfoItemNew(self):
        """Test UpdateInfoItemNew"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()