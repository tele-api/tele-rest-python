# InlineQueryResultAudio

Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the audio.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the result, must be *audio* | [default to 'audio']
**id** | **str** | Unique identifier for this result, 1-64 bytes | 
**audio_url** | **str** | A valid URL for the audio file | 
**title** | **str** | Title | 
**caption** | **str** | *Optional*. Caption, 0-1024 characters after entities parsing | [optional] 
**parse_mode** | **str** | *Optional*. Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**performer** | **str** | *Optional*. Performer | [optional] 
**audio_duration** | **int** | *Optional*. Audio duration in seconds | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**input_message_content** | [**InputMessageContent**](InputMessageContent.md) |  | [optional] 

## Example

```python
from tele_rest.models.inline_query_result_audio import InlineQueryResultAudio

# TODO update the JSON string below
json = "{}"
# create an instance of InlineQueryResultAudio from a JSON string
inline_query_result_audio_instance = InlineQueryResultAudio.from_json(json)
# print the JSON string representation of the object
print(InlineQueryResultAudio.to_json())

# convert the object into a dict
inline_query_result_audio_dict = inline_query_result_audio_instance.to_dict()
# create an instance of InlineQueryResultAudio from a dict
inline_query_result_audio_from_dict = InlineQueryResultAudio.from_dict(inline_query_result_audio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


