# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.message_tg_base_db import MessageTgBaseDb

class TestMessageTgBaseDb(unittest.TestCase):
    """MessageTgBaseDb unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MessageTgBaseDb:
        """Test MessageTgBaseDb
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MessageTgBaseDb`
        """
        model = MessageTgBaseDb()
        if include_optional:
            return MessageTgBaseDb(
                id = 56,
                name = '',
                bot_token = '',
                video_id = '',
                text = ''
            )
        else:
            return MessageTgBaseDb(
                id = 56,
                name = '',
                bot_token = '',
        )
        """

    def testMessageTgBaseDb(self):
        """Test MessageTgBaseDb"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
