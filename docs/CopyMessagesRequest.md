# CopyMessagesRequest

Request parameters for copyMessages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only | [optional] 
**direct_messages_topic_id** | **int** | Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat | [optional] 
**from_chat_id** | [**ForwardMessagesRequestFromChatId**](ForwardMessagesRequestFromChatId.md) |  | 
**message_ids** | **List[int]** | A JSON-serialized list of 1-100 identifiers of messages in the chat *from\\_chat\\_id* to copy. The identifiers must be specified in a strictly increasing order. | 
**disable_notification** | **bool** | Sends the messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the sent messages from forwarding and saving | [optional] 
**remove_caption** | **bool** | Pass *True* to copy the messages without their captions | [optional] 

## Example

```python
from tele_rest.models.copy_messages_request import CopyMessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopyMessagesRequest from a JSON string
copy_messages_request_instance = CopyMessagesRequest.from_json(json)
# print the JSON string representation of the object
print(CopyMessagesRequest.to_json())

# convert the object into a dict
copy_messages_request_dict = copy_messages_request_instance.to_dict()
# create an instance of CopyMessagesRequest from a dict
copy_messages_request_from_dict = CopyMessagesRequest.from_dict(copy_messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


