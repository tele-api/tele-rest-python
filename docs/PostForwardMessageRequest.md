# PostForwardMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of the forum; for forum supergroups only | [optional] 
**from_chat_id** | [**PostForwardMessageRequestFromChatId**](PostForwardMessageRequestFromChatId.md) |  | 
**video_start_timestamp** | **int** | New start timestamp for the forwarded video in the message | [optional] 
**disable_notification** | **bool** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the forwarded message from forwarding and saving | [optional] 
**message_id** | **int** | Message identifier in the chat specified in *from\\_chat\\_id* | 

## Example

```python
from tele_rest.models.post_forward_message_request import PostForwardMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostForwardMessageRequest from a JSON string
post_forward_message_request_instance = PostForwardMessageRequest.from_json(json)
# print the JSON string representation of the object
print(PostForwardMessageRequest.to_json())

# convert the object into a dict
post_forward_message_request_dict = post_forward_message_request_instance.to_dict()
# create an instance of PostForwardMessageRequest from a dict
post_forward_message_request_from_dict = PostForwardMessageRequest.from_dict(post_forward_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


