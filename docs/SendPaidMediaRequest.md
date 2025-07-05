# SendPaidMediaRequest

Request parameters for sendPaidMedia

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be sent | [optional] 
**chat_id** | [**SendPaidMediaRequestChatId**](SendPaidMediaRequestChatId.md) |  | 
**star_count** | **int** | The number of Telegram Stars that must be paid to buy access to the media; 1-10000 | 
**media** | [**List[InputPaidMedia]**](InputPaidMedia.md) | A JSON-serialized array describing the media to be sent; up to 10 items | 
**payload** | **str** | Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes. | [optional] 
**caption** | **str** | Media caption, 0-1024 characters after entities parsing | [optional] 
**parse_mode** | **str** | Mode for parsing entities in the media caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**show_caption_above_media** | **bool** | Pass *True*, if the caption must be shown above the message media | [optional] 
**disable_notification** | **bool** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the sent message from forwarding and saving | [optional] 
**allow_paid_broadcast** | **bool** | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot&#39;s balance | [optional] 
**reply_parameters** | [**ReplyParameters**](ReplyParameters.md) |  | [optional] 
**reply_markup** | [**SendMessageRequestReplyMarkup**](SendMessageRequestReplyMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.send_paid_media_request import SendPaidMediaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendPaidMediaRequest from a JSON string
send_paid_media_request_instance = SendPaidMediaRequest.from_json(json)
# print the JSON string representation of the object
print(SendPaidMediaRequest.to_json())

# convert the object into a dict
send_paid_media_request_dict = send_paid_media_request_instance.to_dict()
# create an instance of SendPaidMediaRequest from a dict
send_paid_media_request_from_dict = SendPaidMediaRequest.from_dict(send_paid_media_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


