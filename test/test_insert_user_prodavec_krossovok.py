# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.insert_user_prodavec_krossovok import InsertUserProdavecKrossovok

class TestInsertUserProdavecKrossovok(unittest.TestCase):
    """InsertUserProdavecKrossovok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsertUserProdavecKrossovok:
        """Test InsertUserProdavecKrossovok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsertUserProdavecKrossovok`
        """
        model = InsertUserProdavecKrossovok()
        if include_optional:
            return InsertUserProdavecKrossovok(
                user_id = 56,
                first_name = '',
                username = '',
                subscribe_channel = True
            )
        else:
            return InsertUserProdavecKrossovok(
                user_id = 56,
                first_name = '',
                username = '',
                subscribe_channel = True,
        )
        """

    def testInsertUserProdavecKrossovok(self):
        """Test InsertUserProdavecKrossovok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
