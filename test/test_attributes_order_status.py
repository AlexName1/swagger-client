# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.attributes_order_status import AttributesOrderStatus

class TestAttributesOrderStatus(unittest.TestCase):
    """AttributesOrderStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttributesOrderStatus:
        """Test AttributesOrderStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttributesOrderStatus`
        """
        model = AttributesOrderStatus()
        if include_optional:
            return AttributesOrderStatus(
                is_return = True,
                cdek_number = '',
                number = '',
                status_code = '',
                status_reason_code = '',
                status_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                city_name = '',
                city_code = '',
                code = '',
                is_reverse = True,
                is_client_return = True,
                related_entities = [
                    swagger_client.models.related_entities.RelatedEntities(
                        type = '', 
                        cdek_number = '', 
                        uuid = '', )
                    ]
            )
        else:
            return AttributesOrderStatus(
                is_return = True,
                cdek_number = '',
                status_code = '',
                status_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                code = '',
                is_reverse = True,
                is_client_return = True,
        )
        """

    def testAttributesOrderStatus(self):
        """Test AttributesOrderStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
