# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.scheduler_base_db import SchedulerBaseDb


class TestSchedulerBaseDb(unittest.TestCase):
    """SchedulerBaseDb unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SchedulerBaseDb:
        """Test SchedulerBaseDb
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SchedulerBaseDb`
        """
        model = SchedulerBaseDb()
        if include_optional:
            return SchedulerBaseDb(
                id = 56,
                messages_tg_id = 56,
                users_bots_id = 56,
                trigger_datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                users_bots = swagger_client.models.user_bot_base.UserBotBase(
                    id = 56, 
                    user_id = 56, 
                    bot_token = '', 
                    last_mess = 56, 
                    items = '', 
                    new_user = True, 
                    subscribe_channel = True, 
                    utm_mark_id = 56, ),
                messages_tg = swagger_client.models.message_tg_base.MessageTgBase(
                    id = 56, 
                    name = '', 
                    bot_token = '', 
                    video_id = '', 
                    text = '', )
            )
        else:
            return SchedulerBaseDb(
        )
        """

    def testSchedulerBaseDb(self):
        """Test SchedulerBaseDb"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
