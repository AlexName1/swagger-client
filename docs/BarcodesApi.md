# swagger_client.BarcodesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**insert_api_v1_barcodes_post**](BarcodesApi.md#insert_api_v1_barcodes_post) | **POST** /api/v1/barcodes | Insert


# **insert_api_v1_barcodes_post**
> MessageResponse insert_api_v1_barcodes_post(insert_barcode)

Insert

### Example

* Basic Authentication (HTTPBasic):

```python
import swagger_client
from swagger_client.models.insert_barcode import InsertBarcode
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
    api_instance = swagger_client.BarcodesApi(api_client)
    insert_barcode = swagger_client.InsertBarcode() # InsertBarcode | 

    try:
        # Insert
        api_response = await api_instance.insert_api_v1_barcodes_post(insert_barcode)
        print("The response of BarcodesApi->insert_api_v1_barcodes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarcodesApi->insert_api_v1_barcodes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insert_barcode** | [**InsertBarcode**](InsertBarcode.md)|  | 

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

