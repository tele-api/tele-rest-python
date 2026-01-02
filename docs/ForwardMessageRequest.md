# ForwardMessageRequest

Request parameters for forwardMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only | [optional] 
**direct_messages_topic_id** | **int** | Identifier of the direct messages topic to which the message will be forwarded; required if the message is forwarded to a direct messages chat | [optional] 
**from_chat_id** | [**ForwardMessageRequestFromChatId**](ForwardMessageRequestFromChatId.md) |  | 
**video_start_timestamp** | **int** | New start timestamp for the forwarded video in the message | [optional] 
**disable_notification** | **bool** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the forwarded message from forwarding and saving | [optional] 
**message_effect_id** | **str** | Unique identifier of the message effect to be added to the message; only available when forwarding to private chats | [optional] 
**suggested_post_parameters** | [**SuggestedPostParameters**](SuggestedPostParameters.md) |  | [optional] 
**message_id** | **int** | Message identifier in the chat specified in *from\\_chat\\_id* | 

## Example

```python
from tele_rest.models.forward_message_request import ForwardMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardMessageRequest from a JSON string
forward_message_request_instance = ForwardMessageRequest.from_json(json)
# print the JSON string representation of the object
print(ForwardMessageRequest.to_json())

# convert the object into a dict
forward_message_request_dict = forward_message_request_instance.to_dict()
# create an instance of ForwardMessageRequest from a dict
forward_message_request_from_dict = ForwardMessageRequest.from_dict(forward_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


