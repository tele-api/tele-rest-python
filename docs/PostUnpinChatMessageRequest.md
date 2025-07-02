# PostUnpinChatMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be unpinned | [optional] 
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**message_id** | **int** | Identifier of the message to unpin. Required if *business\\_connection\\_id* is specified. If not specified, the most recent pinned message (by sending date) will be unpinned. | [optional] 

## Example

```python
from tele_rest.models.post_unpin_chat_message_request import PostUnpinChatMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostUnpinChatMessageRequest from a JSON string
post_unpin_chat_message_request_instance = PostUnpinChatMessageRequest.from_json(json)
# print the JSON string representation of the object
print(PostUnpinChatMessageRequest.to_json())

# convert the object into a dict
post_unpin_chat_message_request_dict = post_unpin_chat_message_request_instance.to_dict()
# create an instance of PostUnpinChatMessageRequest from a dict
post_unpin_chat_message_request_from_dict = PostUnpinChatMessageRequest.from_dict(post_unpin_chat_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


