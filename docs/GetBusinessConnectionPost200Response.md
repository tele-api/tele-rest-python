# GetBusinessConnectionPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**BusinessConnection**](BusinessConnection.md) |  | 

## Example

```python
from tele_rest.models.get_business_connection_post200_response import GetBusinessConnectionPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBusinessConnectionPost200Response from a JSON string
get_business_connection_post200_response_instance = GetBusinessConnectionPost200Response.from_json(json)
# print the JSON string representation of the object
print(GetBusinessConnectionPost200Response.to_json())

# convert the object into a dict
get_business_connection_post200_response_dict = get_business_connection_post200_response_instance.to_dict()
# create an instance of GetBusinessConnectionPost200Response from a dict
get_business_connection_post200_response_from_dict = GetBusinessConnectionPost200Response.from_dict(get_business_connection_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


