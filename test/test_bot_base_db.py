# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.bot_base_db import BotBaseDb


class TestBotBaseDb(unittest.TestCase):
    """BotBaseDb unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BotBaseDb:
        """Test BotBaseDb
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `BotBaseDb`
        """
        model = BotBaseDb()
        if include_optional:
            return BotBaseDb(
                id = 56,
                token = '',
                full_name = '',
                username = '',
                id_bot = 56,
                admin_list = [
                    56
                    ],
                text_channel_url = '',
                support_url = '',
                channel_url = '',
                info_url = '',
                comments_url = ''
            )
        else:
            return BotBaseDb(
        )
        """

    def testBotBaseDb(self):
        """Test BotBaseDb"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
