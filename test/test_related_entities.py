# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.related_entities import RelatedEntities

class TestRelatedEntities(unittest.TestCase):
    """RelatedEntities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelatedEntities:
        """Test RelatedEntities
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelatedEntities`
        """
        model = RelatedEntities()
        if include_optional:
            return RelatedEntities(
                type = '',
                cdek_number = '',
                uuid = ''
            )
        else:
            return RelatedEntities(
                type = '',
                cdek_number = '',
                uuid = '',
        )
        """

    def testRelatedEntities(self):
        """Test RelatedEntities"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()