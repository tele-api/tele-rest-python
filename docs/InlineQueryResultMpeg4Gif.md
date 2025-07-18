# InlineQueryResultMpeg4Gif

Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the animation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the result, must be *mpeg4\\_gif* | [default to 'mpeg4_gif']
**id** | **str** | Unique identifier for this result, 1-64 bytes | 
**mpeg4_url** | **str** | A valid URL for the MPEG4 file | 
**mpeg4_width** | **int** | *Optional*. Video width | [optional] 
**mpeg4_height** | **int** | *Optional*. Video height | [optional] 
**mpeg4_duration** | **int** | *Optional*. Video duration in seconds | [optional] 
**thumbnail_url** | **str** | URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result | 
**thumbnail_mime_type** | **str** | *Optional*. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg” | [optional] [default to 'image/jpeg']
**title** | **str** | *Optional*. Title for the result | [optional] 
**caption** | **str** | *Optional*. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing | [optional] 
**parse_mode** | **str** | *Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**show_caption_above_media** | **bool** | *Optional*. Pass *True*, if the caption must be shown above the message media | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**input_message_content** | [**InputMessageContent**](InputMessageContent.md) |  | [optional] 

## Example

```python
from tele_rest.models.inline_query_result_mpeg4_gif import InlineQueryResultMpeg4Gif

# TODO update the JSON string below
json = "{}"
# create an instance of InlineQueryResultMpeg4Gif from a JSON string
inline_query_result_mpeg4_gif_instance = InlineQueryResultMpeg4Gif.from_json(json)
# print the JSON string representation of the object
print(InlineQueryResultMpeg4Gif.to_json())

# convert the object into a dict
inline_query_result_mpeg4_gif_dict = inline_query_result_mpeg4_gif_instance.to_dict()
# create an instance of InlineQueryResultMpeg4Gif from a dict
inline_query_result_mpeg4_gif_from_dict = InlineQueryResultMpeg4Gif.from_dict(inline_query_result_mpeg4_gif_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


