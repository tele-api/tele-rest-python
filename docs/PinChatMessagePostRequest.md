# PinChatMessagePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be pinned | [optional] 
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**message_id** | **int** | Identifier of a message to pin | 
**disable_notification** | **bool** | Pass *True* if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats. | [optional] 

## Example

```python
from tele_rest.models.pin_chat_message_post_request import PinChatMessagePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PinChatMessagePostRequest from a JSON string
pin_chat_message_post_request_instance = PinChatMessagePostRequest.from_json(json)
# print the JSON string representation of the object
print(PinChatMessagePostRequest.to_json())

# convert the object into a dict
pin_chat_message_post_request_dict = pin_chat_message_post_request_instance.to_dict()
# create an instance of PinChatMessagePostRequest from a dict
pin_chat_message_post_request_from_dict = PinChatMessagePostRequest.from_dict(pin_chat_message_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


