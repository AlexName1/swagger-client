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

from swagger_client.models.model_count import ModelCount

class TestModelCount(unittest.TestCase):
    """ModelCount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelCount:
        """Test ModelCount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelCount`
        """
        model = ModelCount()
        if include_optional:
            return ModelCount(
                model = '',
                count = 56
            )
        else:
            return ModelCount(
                model = '',
                count = 56,
        )
        """

    def testModelCount(self):
        """Test ModelCount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
