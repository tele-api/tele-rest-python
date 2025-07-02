# CopyMessagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[MessageId]**](MessageId.md) |  | 

## Example

```python
from tele_rest.models.copy_messages_response import CopyMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CopyMessagesResponse from a JSON string
copy_messages_response_instance = CopyMessagesResponse.from_json(json)
# print the JSON string representation of the object
print(CopyMessagesResponse.to_json())

# convert the object into a dict
copy_messages_response_dict = copy_messages_response_instance.to_dict()
# create an instance of CopyMessagesResponse from a dict
copy_messages_response_from_dict = CopyMessagesResponse.from_dict(copy_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


