# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.utm_mark_base import UtmMarkBase


class TestUtmMarkBase(unittest.TestCase):
    """UtmMarkBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UtmMarkBase:
        """Test UtmMarkBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UtmMarkBase`
        """
        model = UtmMarkBase()
        if include_optional:
            return UtmMarkBase(
                id = 56,
                name = '',
                affiliate_program_id = 56
            )
        else:
            return UtmMarkBase(
        )
        """

    def testUtmMarkBase(self):
        """Test UtmMarkBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
