# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.size_base import SizeBase


class TestSizeBase(unittest.TestCase):
    """SizeBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SizeBase:
        """Test SizeBase
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SizeBase`
        """
        model = SizeBase()
        if include_optional:
            return SizeBase(
                id = 56,
                value = ''
            )
        else:
            return SizeBase(
        )
        """

    def testSizeBase(self):
        """Test SizeBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
