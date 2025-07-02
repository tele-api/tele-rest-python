# UnpinChatMessageRequest

Request parameters for unpinChatMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be unpinned | [optional] 
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**message_id** | **int** | Identifier of the message to unpin. Required if *business\\_connection\\_id* is specified. If not specified, the most recent pinned message (by sending date) will be unpinned. | [optional] 

## Example

```python
from tele_rest.models.unpin_chat_message_request import UnpinChatMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnpinChatMessageRequest from a JSON string
unpin_chat_message_request_instance = UnpinChatMessageRequest.from_json(json)
# print the JSON string representation of the object
print(UnpinChatMessageRequest.to_json())

# convert the object into a dict
unpin_chat_message_request_dict = unpin_chat_message_request_instance.to_dict()
# create an instance of UnpinChatMessageRequest from a dict
unpin_chat_message_request_from_dict = UnpinChatMessageRequest.from_dict(unpin_chat_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


