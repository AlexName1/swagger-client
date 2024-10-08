# swagger_client.InfoItemsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_api_v1_info_items_token_put**](InfoItemsApi.md#update_api_v1_info_items_token_put) | **PUT** /api/v1/info-items/{token} | Update
[**update_new_api_v1_info_items_token_new_put**](InfoItemsApi.md#update_new_api_v1_info_items_token_new_put) | **PUT** /api/v1/info-items/{token}/new | Update New


# **update_api_v1_info_items_token_put**
> MessageResponse update_api_v1_info_items_token_put(token, info_item_update)

Update

### Example

* Basic Authentication (HTTPBasic):

```python
import swagger_client
from swagger_client.models.info_item_update import InfoItemUpdate
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
    api_instance = swagger_client.InfoItemsApi(api_client)
    token = 'token_example' # str | 
    info_item_update = swagger_client.InfoItemUpdate() # InfoItemUpdate | 

    try:
        # Update
        api_response = await api_instance.update_api_v1_info_items_token_put(token, info_item_update)
        print("The response of InfoItemsApi->update_api_v1_info_items_token_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoItemsApi->update_api_v1_info_items_token_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **info_item_update** | [**InfoItemUpdate**](InfoItemUpdate.md)|  | 

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

# **update_new_api_v1_info_items_token_new_put**
> MessageResponse update_new_api_v1_info_items_token_new_put(token, info_item_update_new)

Update New

### Example

* Basic Authentication (HTTPBasic):

```python
import swagger_client
from swagger_client.models.info_item_update_new import InfoItemUpdateNew
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
    api_instance = swagger_client.InfoItemsApi(api_client)
    token = 'token_example' # str | 
    info_item_update_new = swagger_client.InfoItemUpdateNew() # InfoItemUpdateNew | 

    try:
        # Update New
        api_response = await api_instance.update_new_api_v1_info_items_token_new_put(token, info_item_update_new)
        print("The response of InfoItemsApi->update_new_api_v1_info_items_token_new_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoItemsApi->update_new_api_v1_info_items_token_new_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **info_item_update_new** | [**InfoItemUpdateNew**](InfoItemUpdateNew.md)|  | 

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

