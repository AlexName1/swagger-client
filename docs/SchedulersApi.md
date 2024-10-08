# swagger_client.SchedulersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v1_schedulers_scheduler_id_delete**](SchedulersApi.md#delete_api_v1_schedulers_scheduler_id_delete) | **DELETE** /api/v1/schedulers/{scheduler_id} | Delete
[**get_api_v1_schedulers_get**](SchedulersApi.md#get_api_v1_schedulers_get) | **GET** /api/v1/schedulers | Get
[**insert_api_v1_schedulers_post**](SchedulersApi.md#insert_api_v1_schedulers_post) | **POST** /api/v1/schedulers | Insert


# **delete_api_v1_schedulers_scheduler_id_delete**
> MessageResponse delete_api_v1_schedulers_scheduler_id_delete(scheduler_id)

Delete

### Example

* Basic Authentication (HTTPBasic):

```python
import swagger_client
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
    api_instance = swagger_client.SchedulersApi(api_client)
    scheduler_id = 56 # int | 

    try:
        # Delete
        api_response = await api_instance.delete_api_v1_schedulers_scheduler_id_delete(scheduler_id)
        print("The response of SchedulersApi->delete_api_v1_schedulers_scheduler_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulersApi->delete_api_v1_schedulers_scheduler_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduler_id** | **int**|  | 

### Return type

[**MessageResponse**](MessageResponse.md)

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

# **get_api_v1_schedulers_get**
> List[SchedulerBaseDb] get_api_v1_schedulers_get(token)

Get

### Example

* Basic Authentication (HTTPBasic):

```python
import swagger_client
from swagger_client.models.scheduler_base_db import SchedulerBaseDb
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
    api_instance = swagger_client.SchedulersApi(api_client)
    token = 'token_example' # str | 

    try:
        # Get
        api_response = await api_instance.get_api_v1_schedulers_get(token)
        print("The response of SchedulersApi->get_api_v1_schedulers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulersApi->get_api_v1_schedulers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**List[SchedulerBaseDb]**](SchedulerBaseDb.md)

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

# **insert_api_v1_schedulers_post**
> int insert_api_v1_schedulers_post(insert_scheduler)

Insert

### Example

* Basic Authentication (HTTPBasic):

```python
import swagger_client
from swagger_client.models.insert_scheduler import InsertScheduler
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
    api_instance = swagger_client.SchedulersApi(api_client)
    insert_scheduler = swagger_client.InsertScheduler() # InsertScheduler | 

    try:
        # Insert
        api_response = await api_instance.insert_api_v1_schedulers_post(insert_scheduler)
        print("The response of SchedulersApi->insert_api_v1_schedulers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulersApi->insert_api_v1_schedulers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insert_scheduler** | [**InsertScheduler**](InsertScheduler.md)|  | 

### Return type

**int**

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

