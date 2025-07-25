# InlineQueryResultCachedVideo

Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the video.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the result, must be *video* | [default to 'video']
**id** | **str** | Unique identifier for this result, 1-64 bytes | 
**video_file_id** | **str** | A valid file identifier for the video file | 
**title** | **str** | Title for the result | 
**description** | **str** | *Optional*. Short description of the result | [optional] 
**caption** | **str** | *Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing | [optional] 
**parse_mode** | **str** | *Optional*. Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**show_caption_above_media** | **bool** | *Optional*. Pass *True*, if the caption must be shown above the message media | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**input_message_content** | [**InputMessageContent**](InputMessageContent.md) |  | [optional] 

## Example

```python
from tele_rest.models.inline_query_result_cached_video import InlineQueryResultCachedVideo

# TODO update the JSON string below
json = "{}"
# create an instance of InlineQueryResultCachedVideo from a JSON string
inline_query_result_cached_video_instance = InlineQueryResultCachedVideo.from_json(json)
# print the JSON string representation of the object
print(InlineQueryResultCachedVideo.to_json())

# convert the object into a dict
inline_query_result_cached_video_dict = inline_query_result_cached_video_instance.to_dict()
# create an instance of InlineQueryResultCachedVideo from a dict
inline_query_result_cached_video_from_dict = InlineQueryResultCachedVideo.from_dict(inline_query_result_cached_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


