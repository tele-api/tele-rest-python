# InlineQueryResultCachedGif

Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with specified content instead of the animation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the result, must be *gif* | [default to 'gif']
**id** | **str** | Unique identifier for this result, 1-64 bytes | 
**gif_file_id** | **str** | A valid file identifier for the GIF file | 
**title** | **str** | *Optional*. Title for the result | [optional] 
**caption** | **str** | *Optional*. Caption of the GIF file to be sent, 0-1024 characters after entities parsing | [optional] 
**parse_mode** | **str** | *Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**show_caption_above_media** | **bool** | *Optional*. Pass *True*, if the caption must be shown above the message media | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**input_message_content** | [**InputMessageContent**](InputMessageContent.md) |  | [optional] 

## Example

```python
from tele_rest.models.inline_query_result_cached_gif import InlineQueryResultCachedGif

# TODO update the JSON string below
json = "{}"
# create an instance of InlineQueryResultCachedGif from a JSON string
inline_query_result_cached_gif_instance = InlineQueryResultCachedGif.from_json(json)
# print the JSON string representation of the object
print(InlineQueryResultCachedGif.to_json())

# convert the object into a dict
inline_query_result_cached_gif_dict = inline_query_result_cached_gif_instance.to_dict()
# create an instance of InlineQueryResultCachedGif from a dict
inline_query_result_cached_gif_from_dict = InlineQueryResultCachedGif.from_dict(inline_query_result_cached_gif_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


