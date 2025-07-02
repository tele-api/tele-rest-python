# SendLocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_location_response import SendLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendLocationResponse from a JSON string
send_location_response_instance = SendLocationResponse.from_json(json)
# print the JSON string representation of the object
print(SendLocationResponse.to_json())

# convert the object into a dict
send_location_response_dict = send_location_response_instance.to_dict()
# create an instance of SendLocationResponse from a dict
send_location_response_from_dict = SendLocationResponse.from_dict(send_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


