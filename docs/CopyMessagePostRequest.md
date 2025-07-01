# CopyMessagePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of the forum; for forum supergroups only | [optional] 
**from_chat_id** | [**ForwardMessagePostRequestFromChatId**](ForwardMessagePostRequestFromChatId.md) |  | 
**message_id** | **int** | Message identifier in the chat specified in *from\\_chat\\_id* | 
**video_start_timestamp** | **int** | New start timestamp for the copied video in the message | [optional] 
**caption** | **str** | New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept | [optional] 
**parse_mode** | **str** | Mode for parsing entities in the new caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of *parse\\_mode* | [optional] 
**show_caption_above_media** | **bool** | Pass *True*, if the caption must be shown above the message media. Ignored if a new caption isn&#39;t specified. | [optional] 
**disable_notification** | **bool** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the sent message from forwarding and saving | [optional] 
**allow_paid_broadcast** | **bool** | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot&#39;s balance | [optional] 
**reply_parameters** | [**ReplyParameters**](ReplyParameters.md) |  | [optional] 
**reply_markup** | [**SendMessagePostRequestReplyMarkup**](SendMessagePostRequestReplyMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.copy_message_post_request import CopyMessagePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopyMessagePostRequest from a JSON string
copy_message_post_request_instance = CopyMessagePostRequest.from_json(json)
# print the JSON string representation of the object
print(CopyMessagePostRequest.to_json())

# convert the object into a dict
copy_message_post_request_dict = copy_message_post_request_instance.to_dict()
# create an instance of CopyMessagePostRequest from a dict
copy_message_post_request_from_dict = CopyMessagePostRequest.from_dict(copy_message_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


