# CopyMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**MessageId**](MessageId.md) |  | 

## Example

```python
from tele_rest.models.copy_message_response import CopyMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CopyMessageResponse from a JSON string
copy_message_response_instance = CopyMessageResponse.from_json(json)
# print the JSON string representation of the object
print(CopyMessageResponse.to_json())

# convert the object into a dict
copy_message_response_dict = copy_message_response_instance.to_dict()
# create an instance of CopyMessageResponse from a dict
copy_message_response_from_dict = CopyMessageResponse.from_dict(copy_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


