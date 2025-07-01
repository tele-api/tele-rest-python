# GetBusinessConnectionPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 

## Example

```python
from tele_rest.models.get_business_connection_post_request import GetBusinessConnectionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetBusinessConnectionPostRequest from a JSON string
get_business_connection_post_request_instance = GetBusinessConnectionPostRequest.from_json(json)
# print the JSON string representation of the object
print(GetBusinessConnectionPostRequest.to_json())

# convert the object into a dict
get_business_connection_post_request_dict = get_business_connection_post_request_instance.to_dict()
# create an instance of GetBusinessConnectionPostRequest from a dict
get_business_connection_post_request_from_dict = GetBusinessConnectionPostRequest.from_dict(get_business_connection_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


