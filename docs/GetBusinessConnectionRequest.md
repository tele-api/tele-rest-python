# GetBusinessConnectionRequest

Request parameters for getBusinessConnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 

## Example

```python
from tele_rest.models.get_business_connection_request import GetBusinessConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetBusinessConnectionRequest from a JSON string
get_business_connection_request_instance = GetBusinessConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(GetBusinessConnectionRequest.to_json())

# convert the object into a dict
get_business_connection_request_dict = get_business_connection_request_instance.to_dict()
# create an instance of GetBusinessConnectionRequest from a dict
get_business_connection_request_from_dict = GetBusinessConnectionRequest.from_dict(get_business_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


