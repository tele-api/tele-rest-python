# SendAudioRequest

Request parameters for sendAudio

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be sent | [optional] 
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only | [optional] 
**direct_messages_topic_id** | **int** | Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat | [optional] 
**audio** | **str** |  | 
**caption** | **str** | Audio caption, 0-1024 characters after entities parsing | [optional] 
**parse_mode** | **str** | Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**duration** | **int** | Duration of the audio in seconds | [optional] 
**performer** | **str** | Performer | [optional] 
**title** | **str** | Track name | [optional] 
**thumbnail** | **str** |  | [optional] 
**disable_notification** | **bool** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the sent message from forwarding and saving | [optional] 
**allow_paid_broadcast** | **bool** | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot&#39;s balance | [optional] 
**message_effect_id** | **str** | Unique identifier of the message effect to be added to the message; for private chats only | [optional] 
**suggested_post_parameters** | [**SuggestedPostParameters**](SuggestedPostParameters.md) |  | [optional] 
**reply_parameters** | [**ReplyParameters**](ReplyParameters.md) |  | [optional] 
**reply_markup** | [**SendMessageRequestReplyMarkup**](SendMessageRequestReplyMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.send_audio_request import SendAudioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendAudioRequest from a JSON string
send_audio_request_instance = SendAudioRequest.from_json(json)
# print the JSON string representation of the object
print(SendAudioRequest.to_json())

# convert the object into a dict
send_audio_request_dict = send_audio_request_instance.to_dict()
# create an instance of SendAudioRequest from a dict
send_audio_request_from_dict = SendAudioRequest.from_dict(send_audio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


