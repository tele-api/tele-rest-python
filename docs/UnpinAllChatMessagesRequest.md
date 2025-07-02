# UnpinAllChatMessagesRequest

Request parameters for unpinAllChatMessages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.unpin_all_chat_messages_request import UnpinAllChatMessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnpinAllChatMessagesRequest from a JSON string
unpin_all_chat_messages_request_instance = UnpinAllChatMessagesRequest.from_json(json)
# print the JSON string representation of the object
print(UnpinAllChatMessagesRequest.to_json())

# convert the object into a dict
unpin_all_chat_messages_request_dict = unpin_all_chat_messages_request_instance.to_dict()
# create an instance of UnpinAllChatMessagesRequest from a dict
unpin_all_chat_messages_request_from_dict = UnpinAllChatMessagesRequest.from_dict(unpin_all_chat_messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


