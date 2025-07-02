# PostPinChatMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be pinned | [optional] 
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**message_id** | **int** | Identifier of a message to pin | 
**disable_notification** | **bool** | Pass *True* if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats. | [optional] 

## Example

```python
from tele_rest.models.post_pin_chat_message_request import PostPinChatMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPinChatMessageRequest from a JSON string
post_pin_chat_message_request_instance = PostPinChatMessageRequest.from_json(json)
# print the JSON string representation of the object
print(PostPinChatMessageRequest.to_json())

# convert the object into a dict
post_pin_chat_message_request_dict = post_pin_chat_message_request_instance.to_dict()
# create an instance of PostPinChatMessageRequest from a dict
post_pin_chat_message_request_from_dict = PostPinChatMessageRequest.from_dict(post_pin_chat_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


