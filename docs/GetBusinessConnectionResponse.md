# GetBusinessConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**BusinessConnection**](BusinessConnection.md) |  | 

## Example

```python
from tele_rest.models.get_business_connection_response import GetBusinessConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBusinessConnectionResponse from a JSON string
get_business_connection_response_instance = GetBusinessConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(GetBusinessConnectionResponse.to_json())

# convert the object into a dict
get_business_connection_response_dict = get_business_connection_response_instance.to_dict()
# create an instance of GetBusinessConnectionResponse from a dict
get_business_connection_response_from_dict = GetBusinessConnectionResponse.from_dict(get_business_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


