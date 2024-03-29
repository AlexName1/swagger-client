# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.purchase_base_db import PurchaseBaseDb


class TestPurchaseBaseDb(unittest.TestCase):
    """PurchaseBaseDb unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PurchaseBaseDb:
        """Test PurchaseBaseDb
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PurchaseBaseDb`
        """
        model = PurchaseBaseDb()
        if include_optional:
            return PurchaseBaseDb(
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
                    email = '', )
            )
        else:
            return PurchaseBaseDb(
        )
        """

    def testPurchaseBaseDb(self):
        """Test PurchaseBaseDb"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
