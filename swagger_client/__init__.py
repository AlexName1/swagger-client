# coding: utf-8

# flake8: noqa

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.9.0"

# import apis into sdk package
from swagger_client.api.barcodes_api import BarcodesApi
from swagger_client.api.baskets_api import BasketsApi
from swagger_client.api.bots_api import BotsApi
from swagger_client.api.categories_api import CategoriesApi
from swagger_client.api.deliveries_cdek_api import DeliveriesCdekApi
from swagger_client.api.info_items_api import InfoItemsApi
from swagger_client.api.items_api import ItemsApi
from swagger_client.api.messages_tg_api import MessagesTgApi
from swagger_client.api.orders_api import OrdersApi
from swagger_client.api.partners_api import PartnersApi
from swagger_client.api.purchases_api import PurchasesApi
from swagger_client.api.quantities_api import QuantitiesApi
from swagger_client.api.schedulers_api import SchedulersApi
from swagger_client.api.sizes_api import SizesApi
from swagger_client.api.users_bots_api import UsersBotsApi
from swagger_client.api.users_prodavec_krossovok_api import UsersProdavecKrossovokApi
from swagger_client.api.waybills_api import WaybillsApi
from swagger_client.api.webhook_api import WebhookApi
from swagger_client.api.yookassa_payments_api import YookassaPaymentsApi

# import ApiClient
from swagger_client.api_response import ApiResponse
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from swagger_client.exceptions import OpenApiException
from swagger_client.exceptions import ApiTypeError
from swagger_client.exceptions import ApiValueError
from swagger_client.exceptions import ApiKeyError
from swagger_client.exceptions import ApiAttributeError
from swagger_client.exceptions import ApiException

# import models into sdk package
from swagger_client.models.attributes import Attributes
from swagger_client.models.attributes_order_status import AttributesOrderStatus
from swagger_client.models.attributes_prealert_closer import AttributesPrealertCloser
from swagger_client.models.attributes_print_form import AttributesPrintForm
from swagger_client.models.barcode_insert import BarcodeInsert
from swagger_client.models.basket_base_db import BasketBaseDb
from swagger_client.models.bot_base import BotBase
from swagger_client.models.bot_base_db import BotBaseDb
from swagger_client.models.brand_count import BrandCount
from swagger_client.models.category_base import CategoryBase
from swagger_client.models.cdek_webhook import CdekWebhook
from swagger_client.models.centimeter_base import CentimeterBase
from swagger_client.models.delivery_cdek_base import DeliveryCdekBase
from swagger_client.models.delivery_cdek_update import DeliveryCdekUpdate
from swagger_client.models.dimension_base import DimensionBase
from swagger_client.models.http_validation_error import HTTPValidationError
from swagger_client.models.info_item_insert import InfoItemInsert
from swagger_client.models.info_item_update import InfoItemUpdate
from swagger_client.models.info_item_update_new import InfoItemUpdateNew
from swagger_client.models.insert_basket import InsertBasket
from swagger_client.models.insert_bot import InsertBot
from swagger_client.models.insert_message_tg import InsertMessageTg
from swagger_client.models.insert_order import InsertOrder
from swagger_client.models.insert_scheduler import InsertScheduler
from swagger_client.models.insert_user_prodavec_krossovok import InsertUserProdavecKrossovok
from swagger_client.models.item_base import ItemBase
from swagger_client.models.item_base_db import ItemBaseDb
from swagger_client.models.location_inner import LocationInner
from swagger_client.models.message_tg_base import MessageTgBase
from swagger_client.models.message_tg_base_db import MessageTgBaseDb
from swagger_client.models.model_count import ModelCount
from swagger_client.models.order_base import OrderBase
from swagger_client.models.order_base_db import OrderBaseDb
from swagger_client.models.partner_base import PartnerBase
from swagger_client.models.purchase_base_db import PurchaseBaseDb
from swagger_client.models.quantity_base import QuantityBase
from swagger_client.models.quantity_base_db import QuantityBaseDb
from swagger_client.models.related_entities import RelatedEntities
from swagger_client.models.scheduler_base_db import SchedulerBaseDb
from swagger_client.models.size_base import SizeBase
from swagger_client.models.size_base_db import SizeBaseDb
from swagger_client.models.stock_base import StockBase
from swagger_client.models.update_purchase import UpdatePurchase
from swagger_client.models.update_user_bot_mess import UpdateUserBotMess
from swagger_client.models.user_base_db import UserBaseDb
from swagger_client.models.user_bot_base import UserBotBase
from swagger_client.models.user_bot_base_db import UserBotBaseDb
from swagger_client.models.user_bot_base_db_start import UserBotBaseDbStart
from swagger_client.models.user_prodavec_krossovok_base_db import UserProdavecKrossovokBaseDb
from swagger_client.models.utm_mark_base import UtmMarkBase
from swagger_client.models.validation_error import ValidationError
from swagger_client.models.waybill_update import WaybillUpdate
from swagger_client.models.yookassa_payment_base import YookassaPaymentBase
from swagger_client.models.yookassa_payment_insert import YookassaPaymentInsert
