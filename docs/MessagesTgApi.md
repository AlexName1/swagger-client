# swagger_client.MessagesTgApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_messages_tg_name_get**](MessagesTgApi.md#get_api_v1_messages_tg_name_get) | **GET** /api/v1/messages-tg/{name} | Get
[**insert_or_update_api_v1_messages_tg_post**](MessagesTgApi.md#insert_or_update_api_v1_messages_tg_post) | **POST** /api/v1/messages-tg | Insert Or Update


# **get_api_v1_messages_tg_name_get**
> MessageTgBaseDb get_api_v1_messages_tg_name_get(name, token)

Get

### Example

* Basic Authentication (HTTPBasic):

```python
import swagger_client
from swagger_client.models.message_tg_base_db import MessageTgBaseDb
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
    api_instance = swagger_client.MessagesTgApi(api_client)
    name = 'name_example' # str | 
    token = 'token_example' # str | 

    try:
        # Get
        api_response = await api_instance.get_api_v1_messages_tg_name_get(name, token)
        print("The response of MessagesTgApi->get_api_v1_messages_tg_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesTgApi->get_api_v1_messages_tg_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **token** | **str**|  | 

### Return type

[**MessageTgBaseDb**](MessageTgBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_or_update_api_v1_messages_tg_post**
> MessageResponse insert_or_update_api_v1_messages_tg_post(token, insert_message_tg)

Insert Or Update

### Example

* Basic Authentication (HTTPBasic):

```python
import swagger_client
from swagger_client.models.insert_message_tg import InsertMessageTg
from swagger_client.models.message_response import MessageResponse
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
    api_instance = swagger_client.MessagesTgApi(api_client)
    token = 'token_example' # str | 
    insert_message_tg = swagger_client.InsertMessageTg() # InsertMessageTg | 

    try:
        # Insert Or Update
        api_response = await api_instance.insert_or_update_api_v1_messages_tg_post(token, insert_message_tg)
        print("The response of MessagesTgApi->insert_or_update_api_v1_messages_tg_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesTgApi->insert_or_update_api_v1_messages_tg_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **insert_message_tg** | [**InsertMessageTg**](InsertMessageTg.md)|  | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

