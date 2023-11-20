# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.order_base_db import OrderBaseDb


class TestOrderBaseDb(unittest.TestCase):
    """OrderBaseDb unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderBaseDb:
        """Test OrderBaseDb
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderBaseDb`
        """
        model = OrderBaseDb()
        if include_optional:
            return OrderBaseDb(
                id = 56,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user_bot_id = 56,
                buyer = '',
                delivery = '',
                address = '',
                phone = '',
                checking = True,
                payment_receipt = '',
                comment = '',
                partner = True,
                paid = True,
                purchases = [
                    swagger_client.models.purchase_base_db.PurchaseBaseDb(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        buyer = '', 
                        code = '', 
                        price = 56, 
                        delivery = '', 
                        address = '', 
                        phone = '', 
                        checking = True, 
                        pod = 56, 
                        invoice = '', 
                        comment = '', 
                        status = 56, 
                        add_info = '', 
                        user_id = 56, 
                        add_photo = '', 
                        partner = True, 
                        paid = True, 
                        delivery_cdek_id = 56, 
                        approve_size = True, 
                        size_id = 56, 
                        bot_id = 56, 
                        order_id = 56, 
                        delivery_cdek_photo_tg_file_id = '', 
                        item = swagger_client.models.item_base.ItemBase(
                            id = 56, 
                            code = '', 
                            changed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            active = True, 
                            brand = '', 
                            model = '', 
                            title = '', 
                            retail_price = 56, 
                            drop_price = 56, 
                            link = '', 
                            photos = '', 
                            season = '', 
                            color = '', 
                            discount_price = 56, 
                            new = True, 
                            code_hash = '', 
                            category_id = '', 
                            manufacturer_country = '', 
                            material = '', 
                            dimension_id = 56, 
                            photo_path_tg = '', ), 
                        order = swagger_client.models.order_base.OrderBase(
                            id = 56, 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            user_bot_id = 56, 
                            buyer = '', 
                            delivery = '', 
                            address = '', 
                            phone = '', 
                            checking = True, 
                            payment_receipt = '', 
                            comment = '', 
                            partner = True, 
                            paid = True, ), 
                        delivery_cdek = swagger_client.models.delivery_cdek_base.DeliveryCdekBase(
                            id = 56, 
                            uuid_id = '', 
                            tariff_code = 56, 
                            delivery_point = '', 
                            create_datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            status = 56, 
                            status_cdek = '', 
                            cdek_number = '', 
                            photo_tg_file_id = '', 
                            invoice_tg_file_id = '', 
                            courier_to_location = '', 
                            stock_id = '', 
                            comment_sender = '', ), 
                        size = swagger_client.models.size_base.SizeBase(
                            id = 56, 
                            value = '', ), 
                        yookassa_payment = swagger_client.models.yookassa_payment_base.YookassaPaymentBase(
                            id = 56, 
                            purchase_id = 56, 
                            payment_id = '', 
                            status = '', 
                            captured_at = '', 
                            email = '', ), )
                    ],
                user_bot = swagger_client.models.user_bot_base_db.UserBotBaseDb(
                    id = 56, 
                    user_id = 56, 
                    bot_token = '', 
                    last_mess = 56, 
                    items = '', 
                    new_user = True, 
                    subscribe_channel = True, 
                    utm_mark_id = 56, 
                    user = swagger_client.models.user_base_db.UserBaseDb(
                        id = 56, 
                        user_id = 56, 
                        first_name = '', 
                        username = '', 
                        stock = swagger_client.models.stock_base.StockBase(
                            id = '', 
                            name = '', 
                            user_id = 56, 
                            number = 56, 
                            shipment_point = '', ), 
                        users_bots = [
                            swagger_client.models.user_bot_base.UserBotBase(
                                id = 56, 
                                user_id = 56, 
                                bot_token = '', 
                                last_mess = 56, 
                                items = '', 
                                new_user = True, 
                                subscribe_channel = True, 
                                utm_mark_id = 56, )
                            ], ), 
                    bot = swagger_client.models.bot_base.BotBase(
                        id = 56, 
                        token = '', 
                        full_name = '', 
                        username = '', 
                        id_bot = 56, 
                        admin_list = '', 
                        text_channel_url = '', 
                        support_url = '', 
                        channel_url = '', 
                        info_url = '', 
                        comments_url = '', ), 
                    partner = swagger_client.models.partner_base.PartnerBase(
                        id = 56, 
                        user_bot_id = 56, 
                        reserve_balance = '', 
                        card_number = '', 
                        telephone = '', 
                        full_name = '', 
                        bank_name = '', ), 
                    utm_mark = swagger_client.models.utm_mark_base.UtmMarkBase(
                        id = 56, 
                        name = '', 
                        affiliate_program_id = 56, ), 
                    orders = [
                        swagger_client.models.order_base.OrderBase(
                            id = 56, 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            user_bot_id = 56, 
                            buyer = '', 
                            delivery = '', 
                            address = '', 
                            phone = '', 
                            checking = True, 
                            payment_receipt = '', 
                            comment = '', 
                            paid = True, )
                        ], )
            )
        else:
            return OrderBaseDb(
        )
        """

    def testOrderBaseDb(self):
        """Test OrderBaseDb"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
