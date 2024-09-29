# swagger-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.27.0
- Generator version: 7.4.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/AlexName1/swagger-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/AlexName1/swagger-client.git`)

Then import the package:
```python
import swagger_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = swagger_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: HTTPBasic
configuration = swagger_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)


# Enter a context with an instance of the API client
async with swagger_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = swagger_client.BarcodesApi(api_client)
    barcode_insert = swagger_client.BarcodeInsert() # BarcodeInsert | 

    try:
        # Insert
        api_response = await api_instance.insert_api_v1_barcodes_post(barcode_insert)
        print("The response of BarcodesApi->insert_api_v1_barcodes_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BarcodesApi->insert_api_v1_barcodes_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BarcodesApi* | [**insert_api_v1_barcodes_post**](docs/BarcodesApi.md#insert_api_v1_barcodes_post) | **POST** /api/v1/barcodes | Insert
*BasketsApi* | [**delete_one_basket_api_v1_baskets_basket_id_delete**](docs/BasketsApi.md#delete_one_basket_api_v1_baskets_basket_id_delete) | **DELETE** /api/v1/baskets/{basket_id} | Delete One Basket
*BasketsApi* | [**delete_user_basket_api_v1_baskets_users_bots_user_bot_id_delete**](docs/BasketsApi.md#delete_user_basket_api_v1_baskets_users_bots_user_bot_id_delete) | **DELETE** /api/v1/baskets/users_bots/{user_bot_id} | Delete User Basket
*BasketsApi* | [**get_basket_api_v1_baskets_get**](docs/BasketsApi.md#get_basket_api_v1_baskets_get) | **GET** /api/v1/baskets | Get Basket
*BasketsApi* | [**get_count_basket_api_v1_baskets_all_count_get**](docs/BasketsApi.md#get_count_basket_api_v1_baskets_all_count_get) | **GET** /api/v1/baskets/all/count | Get Count Basket
*BasketsApi* | [**get_list_id_basket_api_v1_baskets_all_list_id_get**](docs/BasketsApi.md#get_list_id_basket_api_v1_baskets_all_list_id_get) | **GET** /api/v1/baskets/all/list_id | Get List Id Basket
*BasketsApi* | [**get_one_basket_api_v1_baskets_basket_id_get**](docs/BasketsApi.md#get_one_basket_api_v1_baskets_basket_id_get) | **GET** /api/v1/baskets/{basket_id} | Get One Basket
*BasketsApi* | [**insert_api_v1_baskets_post**](docs/BasketsApi.md#insert_api_v1_baskets_post) | **POST** /api/v1/baskets | Insert
*BotsApi* | [**delete_api_v1_bots_token_delete**](docs/BotsApi.md#delete_api_v1_bots_token_delete) | **DELETE** /api/v1/bots/{token} | Delete
*BotsApi* | [**get_bot_api_v1_bots_token_get**](docs/BotsApi.md#get_bot_api_v1_bots_token_get) | **GET** /api/v1/bots/{token} | Get Bot
*BotsApi* | [**get_bot_by_id_api_v1_bots_ids_bot_id_get**](docs/BotsApi.md#get_bot_by_id_api_v1_bots_ids_bot_id_get) | **GET** /api/v1/bots/ids/{bot_id} | Get Bot By Id
*BotsApi* | [**get_bots_api_v1_bots_get**](docs/BotsApi.md#get_bots_api_v1_bots_get) | **GET** /api/v1/bots | Get Bots
*BotsApi* | [**get_tokens_multibot_api_v1_bots_multibot_tokens_get**](docs/BotsApi.md#get_tokens_multibot_api_v1_bots_multibot_tokens_get) | **GET** /api/v1/bots/multibot/tokens | Get Tokens Multibot
*BotsApi* | [**insert_or_nothing_api_v1_bots_post**](docs/BotsApi.md#insert_or_nothing_api_v1_bots_post) | **POST** /api/v1/bots | Insert Or Nothing
*BotsApi* | [**update_api_v1_bots_patch**](docs/BotsApi.md#update_api_v1_bots_patch) | **PATCH** /api/v1/bots | Update
*CategoriesApi* | [**get_categories_name_api_v1_categories_get**](docs/CategoriesApi.md#get_categories_name_api_v1_categories_get) | **GET** /api/v1/categories | Get Categories Name
*DeliveriesCdekApi* | [**delete_api_v1_deliveries_cdek_delete**](docs/DeliveriesCdekApi.md#delete_api_v1_deliveries_cdek_delete) | **DELETE** /api/v1/deliveries-cdek | Delete
*DeliveriesCdekApi* | [**update_api_v1_deliveries_cdek_put**](docs/DeliveriesCdekApi.md#update_api_v1_deliveries_cdek_put) | **PUT** /api/v1/deliveries-cdek | Update
*InfoItemsApi* | [**update_api_v1_info_items_token_put**](docs/InfoItemsApi.md#update_api_v1_info_items_token_put) | **PUT** /api/v1/info-items/{token} | Update
*InfoItemsApi* | [**update_new_api_v1_info_items_token_new_put**](docs/InfoItemsApi.md#update_new_api_v1_info_items_token_new_put) | **PUT** /api/v1/info-items/{token}/new | Update New
*ItemsApi* | [**get_all_api_v1_items_get**](docs/ItemsApi.md#get_all_api_v1_items_get) | **GET** /api/v1/items | Get All
*ItemsApi* | [**get_brands_and_counts_api_v1_items_category_brands_counts_get**](docs/ItemsApi.md#get_brands_and_counts_api_v1_items_category_brands_counts_get) | **GET** /api/v1/items/{category}/brands-counts | Get Brands And Counts
*ItemsApi* | [**get_count_brand_api_v1_items_category_brand_count_get**](docs/ItemsApi.md#get_count_brand_api_v1_items_category_brand_count_get) | **GET** /api/v1/items/{category}/{brand}/count | Get Count Brand
*ItemsApi* | [**get_count_models_api_v1_items_category_brand_count_models_get**](docs/ItemsApi.md#get_count_models_api_v1_items_category_brand_count_models_get) | **GET** /api/v1/items/{category}/{brand}/count-models | Get Count Models
*ItemsApi* | [**get_item_api_v1_items_code_token_one_get**](docs/ItemsApi.md#get_item_api_v1_items_code_token_one_get) | **GET** /api/v1/items/{code}/{token}/one | Get Item
*ItemsApi* | [**get_item_new_api_v1_items_code_token_one_new_get**](docs/ItemsApi.md#get_item_new_api_v1_items_code_token_one_new_get) | **GET** /api/v1/items/{code}/{token}/one_new | Get Item New
*ItemsApi* | [**get_item_selectinload_size_api_v1_items_code_token_load_size_get**](docs/ItemsApi.md#get_item_selectinload_size_api_v1_items_code_token_load_size_get) | **GET** /api/v1/items/{code}/{token}/load-size | Get Item Selectinload Size
*ItemsApi* | [**get_items_action_new_codes_api_v1_items_token_all_new_codes_get**](docs/ItemsApi.md#get_items_action_new_codes_api_v1_items_token_all_new_codes_get) | **GET** /api/v1/items/{token}/all_new_codes | Get Items Action New Codes
*ItemsApi* | [**get_items_codes_api_v1_items_category_brand_codes_get**](docs/ItemsApi.md#get_items_codes_api_v1_items_category_brand_codes_get) | **GET** /api/v1/items/{category}/{brand}/codes | Get Items Codes
*ItemsApi* | [**get_models_and_counts_api_v1_items_category_brand_models_counts_get**](docs/ItemsApi.md#get_models_and_counts_api_v1_items_category_brand_models_counts_get) | **GET** /api/v1/items/{category}/{brand}/models-counts | Get Models And Counts
*MessagesTgApi* | [**get_api_v1_messages_tg_name_get**](docs/MessagesTgApi.md#get_api_v1_messages_tg_name_get) | **GET** /api/v1/messages-tg/{name} | Get
*MessagesTgApi* | [**insert_or_update_api_v1_messages_tg_post**](docs/MessagesTgApi.md#insert_or_update_api_v1_messages_tg_post) | **POST** /api/v1/messages-tg | Insert Or Update
*OrdersApi* | [**delete_order_api_v1_orders_order_id_delete**](docs/OrdersApi.md#delete_order_api_v1_orders_order_id_delete) | **DELETE** /api/v1/orders/{order_id} | Delete Order
*OrdersApi* | [**get_active_orders_api_v1_orders_get**](docs/OrdersApi.md#get_active_orders_api_v1_orders_get) | **GET** /api/v1/orders | Get Active Orders
*OrdersApi* | [**get_count_orders_api_v1_orders_count_get**](docs/OrdersApi.md#get_count_orders_api_v1_orders_count_get) | **GET** /api/v1/orders/count | Get Count Orders
*OrdersApi* | [**get_count_orders_by_user_id_api_v1_orders_users_user_id_count_get**](docs/OrdersApi.md#get_count_orders_by_user_id_api_v1_orders_users_user_id_count_get) | **GET** /api/v1/orders/users/{user_id}/count | Get Count Orders By User Id
*OrdersApi* | [**get_order_by_id_api_v1_orders_order_id_get**](docs/OrdersApi.md#get_order_by_id_api_v1_orders_order_id_get) | **GET** /api/v1/orders/{order_id} | Get Order By Id
*OrdersApi* | [**get_user_orders_api_v1_orders_users_user_id_get**](docs/OrdersApi.md#get_user_orders_api_v1_orders_users_user_id_get) | **GET** /api/v1/orders/users/{user_id} | Get User Orders
*OrdersApi* | [**insert_order_api_v1_orders_post**](docs/OrdersApi.md#insert_order_api_v1_orders_post) | **POST** /api/v1/orders | Insert Order
*OrdersApi* | [**update_order_api_v1_orders_patch**](docs/OrdersApi.md#update_order_api_v1_orders_patch) | **PATCH** /api/v1/orders | Update Order
*PartnersApi* | [**get_partners_user_id_api_v1_partners_get**](docs/PartnersApi.md#get_partners_user_id_api_v1_partners_get) | **GET** /api/v1/partners | Get Partners User Id
*PurchasesApi* | [**delete_purchase_api_v1_purchases_purchase_id_delete**](docs/PurchasesApi.md#delete_purchase_api_v1_purchases_purchase_id_delete) | **DELETE** /api/v1/purchases/{purchase_id} | Delete Purchase
*PurchasesApi* | [**get_all_api_v1_purchases_get**](docs/PurchasesApi.md#get_all_api_v1_purchases_get) | **GET** /api/v1/purchases | Get All
*PurchasesApi* | [**get_purchase_by_id_api_v1_purchases_purchase_id_get**](docs/PurchasesApi.md#get_purchase_by_id_api_v1_purchases_purchase_id_get) | **GET** /api/v1/purchases/{purchase_id} | Get Purchase By Id
*PurchasesApi* | [**update_only_api_v1_purchases_put**](docs/PurchasesApi.md#update_only_api_v1_purchases_put) | **PUT** /api/v1/purchases | Update Only
*QuantitiesApi* | [**insert_or_update_api_v1_quantities_merge_post**](docs/QuantitiesApi.md#insert_or_update_api_v1_quantities_merge_post) | **POST** /api/v1/quantities/merge | Insert Or Update
*SchedulersApi* | [**delete_api_v1_schedulers_scheduler_id_delete**](docs/SchedulersApi.md#delete_api_v1_schedulers_scheduler_id_delete) | **DELETE** /api/v1/schedulers/{scheduler_id} | Delete
*SchedulersApi* | [**get_api_v1_schedulers_get**](docs/SchedulersApi.md#get_api_v1_schedulers_get) | **GET** /api/v1/schedulers | Get
*SchedulersApi* | [**insert_api_v1_schedulers_post**](docs/SchedulersApi.md#insert_api_v1_schedulers_post) | **POST** /api/v1/schedulers | Insert
*SizesApi* | [**get_size_by_id_api_v1_sizes_size_id_get**](docs/SizesApi.md#get_size_by_id_api_v1_sizes_size_id_get) | **GET** /api/v1/sizes/{size_id} | Get Size By Id
*SizesApi* | [**get_sizes_api_v1_sizes_get**](docs/SizesApi.md#get_sizes_api_v1_sizes_get) | **GET** /api/v1/sizes | Get Sizes
*SizesApi* | [**insert_or_nothing_api_v1_sizes_post**](docs/SizesApi.md#insert_or_nothing_api_v1_sizes_post) | **POST** /api/v1/sizes | Insert Or Nothing
*TbankKassesApi* | [**get_tbank_kassa_api_v1_tbank_kasses_token_get**](docs/TbankKassesApi.md#get_tbank_kassa_api_v1_tbank_kasses_token_get) | **GET** /api/v1/tbank-kasses/{token} | Get Tbank Kassa
*TbankKassesApi* | [**insert_api_v1_tbank_kasses_post**](docs/TbankKassesApi.md#insert_api_v1_tbank_kasses_post) | **POST** /api/v1/tbank-kasses | Insert
*TbankPaymentsApi* | [**get_tbank_payment_api_v1_tbank_payments_get**](docs/TbankPaymentsApi.md#get_tbank_payment_api_v1_tbank_payments_get) | **GET** /api/v1/tbank-payments | Get Tbank Payment
*TbankPaymentsApi* | [**insert_api_v1_tbank_payments_post**](docs/TbankPaymentsApi.md#insert_api_v1_tbank_payments_post) | **POST** /api/v1/tbank-payments | Insert
*UsersBotsApi* | [**get_all_ids_users_api_v1_users_bots_ids_get**](docs/UsersBotsApi.md#get_all_ids_users_api_v1_users_bots_ids_get) | **GET** /api/v1/users_bots/ids | Get All Ids Users
*UsersBotsApi* | [**get_count_api_v1_users_bots_count_get**](docs/UsersBotsApi.md#get_count_api_v1_users_bots_count_get) | **GET** /api/v1/users_bots/count | Get Count
*UsersBotsApi* | [**get_only_user_bot_api_v1_users_bots_user_id_only_get**](docs/UsersBotsApi.md#get_only_user_bot_api_v1_users_bots_user_id_only_get) | **GET** /api/v1/users_bots/{user_id}/only | Get Only User Bot
*UsersBotsApi* | [**get_user_bot_api_v1_users_bots_user_id_get**](docs/UsersBotsApi.md#get_user_bot_api_v1_users_bots_user_id_get) | **GET** /api/v1/users_bots/{user_id} | Get User Bot
*UsersBotsApi* | [**get_user_bot_by_id_api_v1_users_bots_ids_user_bot_id_get**](docs/UsersBotsApi.md#get_user_bot_by_id_api_v1_users_bots_ids_user_bot_id_get) | **GET** /api/v1/users_bots/ids/{user_bot_id} | Get User Bot By Id
*UsersBotsApi* | [**get_user_bot_start_api_v1_users_bots_user_id_start_get**](docs/UsersBotsApi.md#get_user_bot_start_api_v1_users_bots_user_id_start_get) | **GET** /api/v1/users_bots/{user_id}/start | Get User Bot Start
*UsersBotsApi* | [**get_user_client_bot_api_v1_users_bots_user_id_client_get**](docs/UsersBotsApi.md#get_user_client_bot_api_v1_users_bots_user_id_client_get) | **GET** /api/v1/users_bots/{user_id}/client | Get User Client Bot
*UsersBotsApi* | [**update_last_mess_api_v1_users_bots_mess_put**](docs/UsersBotsApi.md#update_last_mess_api_v1_users_bots_mess_put) | **PUT** /api/v1/users_bots/mess | Update Last Mess
*UsersProdavecKrossovokApi* | [**get_all_ids_users_api_v1_users_prodavec_krossovok_ids_get**](docs/UsersProdavecKrossovokApi.md#get_all_ids_users_api_v1_users_prodavec_krossovok_ids_get) | **GET** /api/v1/users-prodavec-krossovok/ids | Get All Ids Users
*UsersProdavecKrossovokApi* | [**get_count_api_v1_users_prodavec_krossovok_count_get**](docs/UsersProdavecKrossovokApi.md#get_count_api_v1_users_prodavec_krossovok_count_get) | **GET** /api/v1/users-prodavec-krossovok/count | Get Count
*UsersProdavecKrossovokApi* | [**get_user_prodavec_krossovok_api_v1_users_prodavec_krossovok_user_id_get**](docs/UsersProdavecKrossovokApi.md#get_user_prodavec_krossovok_api_v1_users_prodavec_krossovok_user_id_get) | **GET** /api/v1/users-prodavec-krossovok/{user_id} | Get User Prodavec Krossovok
*UsersProdavecKrossovokApi* | [**insert_user_prodavec_krossovok_api_v1_users_prodavec_krossovok_post**](docs/UsersProdavecKrossovokApi.md#insert_user_prodavec_krossovok_api_v1_users_prodavec_krossovok_post) | **POST** /api/v1/users-prodavec-krossovok | Insert User Prodavec Krossovok
*WaybillsApi* | [**update_api_v1_waybills_put**](docs/WaybillsApi.md#update_api_v1_waybills_put) | **PUT** /api/v1/waybills | Update
*WebhookApi* | [**webhook_from_cdek_api_v1_webhook_cdek_post**](docs/WebhookApi.md#webhook_from_cdek_api_v1_webhook_cdek_post) | **POST** /api/v1/webhook/cdek | Webhook From Cdek
*YookassaPaymentsApi* | [**insert_api_v1_yookassa_payments_post**](docs/YookassaPaymentsApi.md#insert_api_v1_yookassa_payments_post) | **POST** /api/v1/yookassa-payments | Insert


## Documentation For Models

 - [Attributes](docs/Attributes.md)
 - [AttributesOrderStatus](docs/AttributesOrderStatus.md)
 - [AttributesPrealertCloser](docs/AttributesPrealertCloser.md)
 - [AttributesPrintForm](docs/AttributesPrintForm.md)
 - [BarcodeInsert](docs/BarcodeInsert.md)
 - [BasketBaseDb](docs/BasketBaseDb.md)
 - [BotBase](docs/BotBase.md)
 - [BotBaseDb](docs/BotBaseDb.md)
 - [BrandCount](docs/BrandCount.md)
 - [CategoryBase](docs/CategoryBase.md)
 - [CdekWebhook](docs/CdekWebhook.md)
 - [CentimeterBase](docs/CentimeterBase.md)
 - [DeliveryCdekBase](docs/DeliveryCdekBase.md)
 - [DeliveryCdekUpdate](docs/DeliveryCdekUpdate.md)
 - [DimensionBase](docs/DimensionBase.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [InfoItemUpdate](docs/InfoItemUpdate.md)
 - [InfoItemUpdateNew](docs/InfoItemUpdateNew.md)
 - [InsertBasket](docs/InsertBasket.md)
 - [InsertBot](docs/InsertBot.md)
 - [InsertMessageTg](docs/InsertMessageTg.md)
 - [InsertOrder](docs/InsertOrder.md)
 - [InsertScheduler](docs/InsertScheduler.md)
 - [InsertTBankKassa](docs/InsertTBankKassa.md)
 - [InsertTBankPayment](docs/InsertTBankPayment.md)
 - [InsertUserProdavecKrossovok](docs/InsertUserProdavecKrossovok.md)
 - [ItemBase](docs/ItemBase.md)
 - [ItemBaseDb](docs/ItemBaseDb.md)
 - [LocationInner](docs/LocationInner.md)
 - [MessageResponse](docs/MessageResponse.md)
 - [MessageTgBase](docs/MessageTgBase.md)
 - [MessageTgBaseDb](docs/MessageTgBaseDb.md)
 - [ModelCount](docs/ModelCount.md)
 - [OrderBase](docs/OrderBase.md)
 - [OrderBaseDb](docs/OrderBaseDb.md)
 - [PartnerBase](docs/PartnerBase.md)
 - [PurchaseBaseDb](docs/PurchaseBaseDb.md)
 - [QuantityBase](docs/QuantityBase.md)
 - [QuantityBaseDb](docs/QuantityBaseDb.md)
 - [RelatedEntities](docs/RelatedEntities.md)
 - [SchedulerBaseDb](docs/SchedulerBaseDb.md)
 - [SizeBase](docs/SizeBase.md)
 - [SizeBaseDb](docs/SizeBaseDb.md)
 - [StockBase](docs/StockBase.md)
 - [TBankKassaDb](docs/TBankKassaDb.md)
 - [TBankPaymentDb](docs/TBankPaymentDb.md)
 - [UpdateBot](docs/UpdateBot.md)
 - [UpdateOrder](docs/UpdateOrder.md)
 - [UpdatePurchase](docs/UpdatePurchase.md)
 - [UpdateUserBotMess](docs/UpdateUserBotMess.md)
 - [UserBaseDb](docs/UserBaseDb.md)
 - [UserBotBase](docs/UserBotBase.md)
 - [UserBotBaseDb](docs/UserBotBaseDb.md)
 - [UserBotBaseDbStart](docs/UserBotBaseDbStart.md)
 - [UserProdavecKrossovokBaseDb](docs/UserProdavecKrossovokBaseDb.md)
 - [UtmMarkBase](docs/UtmMarkBase.md)
 - [ValidationError](docs/ValidationError.md)
 - [WaybillUpdate](docs/WaybillUpdate.md)
 - [YookassaPaymentBase](docs/YookassaPaymentBase.md)
 - [YookassaPaymentInsert](docs/YookassaPaymentInsert.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="HTTPBasic"></a>
### HTTPBasic

- **Type**: HTTP basic authentication


## Author




