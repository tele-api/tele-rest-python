# InlineQueryResultPhoto

Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the photo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the result, must be *photo* | [default to 'photo']
**id** | **str** | Unique identifier for this result, 1-64 bytes | 
**photo_url** | **str** | A valid URL of the photo. Photo must be in **JPEG** format. Photo size must not exceed 5MB | 
**thumbnail_url** | **str** | URL of the thumbnail for the photo | 
**photo_width** | **int** | *Optional*. Width of the photo | [optional] 
**photo_height** | **int** | *Optional*. Height of the photo | [optional] 
**title** | **str** | *Optional*. Title for the result | [optional] 
**description** | **str** | *Optional*. Short description of the result | [optional] 
**caption** | **str** | *Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing | [optional] 
**parse_mode** | **str** | *Optional*. Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**show_caption_above_media** | **bool** | *Optional*. Pass *True*, if the caption must be shown above the message media | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**input_message_content** | [**InputMessageContent**](InputMessageContent.md) |  | [optional] 

## Example

```python
from tele_rest.models.inline_query_result_photo import InlineQueryResultPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of InlineQueryResultPhoto from a JSON string
inline_query_result_photo_instance = InlineQueryResultPhoto.from_json(json)
# print the JSON string representation of the object
print(InlineQueryResultPhoto.to_json())

# convert the object into a dict
inline_query_result_photo_dict = inline_query_result_photo_instance.to_dict()
# create an instance of InlineQueryResultPhoto from a dict
inline_query_result_photo_from_dict = InlineQueryResultPhoto.from_dict(inline_query_result_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


