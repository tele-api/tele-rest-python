# SendMediaGroupRequest

Request parameters for sendMediaGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be sent | [optional] 
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only | [optional] 
**direct_messages_topic_id** | **int** | Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat | [optional] 
**media** | [**List[SendMediaGroupRequestMediaInner]**](SendMediaGroupRequestMediaInner.md) | A JSON-serialized array describing messages to be sent, must include 2-10 items | 
**disable_notification** | **bool** | Sends messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the sent messages from forwarding and saving | [optional] 
**allow_paid_broadcast** | **bool** | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot&#39;s balance | [optional] 
**message_effect_id** | **str** | Unique identifier of the message effect to be added to the message; for private chats only | [optional] 
**reply_parameters** | [**ReplyParameters**](ReplyParameters.md) |  | [optional] 

## Example

```python
from tele_rest.models.send_media_group_request import SendMediaGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendMediaGroupRequest from a JSON string
send_media_group_request_instance = SendMediaGroupRequest.from_json(json)
# print the JSON string representation of the object
print(SendMediaGroupRequest.to_json())

# convert the object into a dict
send_media_group_request_dict = send_media_group_request_instance.to_dict()
# create an instance of SendMediaGroupRequest from a dict
send_media_group_request_from_dict = SendMediaGroupRequest.from_dict(send_media_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


