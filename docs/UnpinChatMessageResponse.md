# UnpinChatMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.unpin_chat_message_response import UnpinChatMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnpinChatMessageResponse from a JSON string
unpin_chat_message_response_instance = UnpinChatMessageResponse.from_json(json)
# print the JSON string representation of the object
print(UnpinChatMessageResponse.to_json())

# convert the object into a dict
unpin_chat_message_response_dict = unpin_chat_message_response_instance.to_dict()
# create an instance of UnpinChatMessageResponse from a dict
unpin_chat_message_response_from_dict = UnpinChatMessageResponse.from_dict(unpin_chat_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


