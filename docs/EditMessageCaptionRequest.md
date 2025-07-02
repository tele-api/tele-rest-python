# EditMessageCaptionRequest

Request parameters for editMessageCaption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message to be edited was sent | [optional] 
**chat_id** | [**EditMessageTextRequestChatId**](EditMessageTextRequestChatId.md) |  | [optional] 
**message_id** | **int** | Required if *inline\\_message\\_id* is not specified. Identifier of the message to edit | [optional] 
**inline_message_id** | **str** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message | [optional] 
**caption** | **str** | New caption of the message, 0-1024 characters after entities parsing | [optional] 
**parse_mode** | **str** | Mode for parsing entities in the message caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**show_caption_above_media** | **bool** | Pass *True*, if the caption must be shown above the message media. Supported only for animation, photo and video messages. | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.edit_message_caption_request import EditMessageCaptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageCaptionRequest from a JSON string
edit_message_caption_request_instance = EditMessageCaptionRequest.from_json(json)
# print the JSON string representation of the object
print(EditMessageCaptionRequest.to_json())

# convert the object into a dict
edit_message_caption_request_dict = edit_message_caption_request_instance.to_dict()
# create an instance of EditMessageCaptionRequest from a dict
edit_message_caption_request_from_dict = EditMessageCaptionRequest.from_dict(edit_message_caption_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


