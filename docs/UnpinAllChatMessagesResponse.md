# UnpinAllChatMessagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.unpin_all_chat_messages_response import UnpinAllChatMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnpinAllChatMessagesResponse from a JSON string
unpin_all_chat_messages_response_instance = UnpinAllChatMessagesResponse.from_json(json)
# print the JSON string representation of the object
print(UnpinAllChatMessagesResponse.to_json())

# convert the object into a dict
unpin_all_chat_messages_response_dict = unpin_all_chat_messages_response_instance.to_dict()
# create an instance of UnpinAllChatMessagesResponse from a dict
unpin_all_chat_messages_response_from_dict = UnpinAllChatMessagesResponse.from_dict(unpin_all_chat_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


