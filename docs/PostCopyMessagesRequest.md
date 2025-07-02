# PostCopyMessagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of the forum; for forum supergroups only | [optional] 
**from_chat_id** | [**PostForwardMessagesRequestFromChatId**](PostForwardMessagesRequestFromChatId.md) |  | 
**message_ids** | **List[int]** | A JSON-serialized list of 1-100 identifiers of messages in the chat *from\\_chat\\_id* to copy. The identifiers must be specified in a strictly increasing order. | 
**disable_notification** | **bool** | Sends the messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the sent messages from forwarding and saving | [optional] 
**remove_caption** | **bool** | Pass *True* to copy the messages without their captions | [optional] 

## Example

```python
from tele_rest.models.post_copy_messages_request import PostCopyMessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCopyMessagesRequest from a JSON string
post_copy_messages_request_instance = PostCopyMessagesRequest.from_json(json)
# print the JSON string representation of the object
print(PostCopyMessagesRequest.to_json())

# convert the object into a dict
post_copy_messages_request_dict = post_copy_messages_request_instance.to_dict()
# create an instance of PostCopyMessagesRequest from a dict
post_copy_messages_request_from_dict = PostCopyMessagesRequest.from_dict(post_copy_messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


