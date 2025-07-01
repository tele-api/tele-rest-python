# InlineQueryResultDocument

Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the file. Currently, only **.PDF** and **.ZIP** files can be sent using this method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the result, must be *document* | [default to 'document']
**id** | **str** | Unique identifier for this result, 1-64 bytes | 
**title** | **str** | Title for the result | 
**caption** | **str** | *Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing | [optional] 
**parse_mode** | **str** | *Optional*. Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**document_url** | **str** | A valid URL for the file | 
**mime_type** | **str** | MIME type of the content of the file, either “application/pdf” or “application/zip” | 
**description** | **str** | *Optional*. Short description of the result | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**input_message_content** | [**InputMessageContent**](InputMessageContent.md) |  | [optional] 
**thumbnail_url** | **str** | *Optional*. URL of the thumbnail (JPEG only) for the file | [optional] 
**thumbnail_width** | **int** | *Optional*. Thumbnail width | [optional] 
**thumbnail_height** | **int** | *Optional*. Thumbnail height | [optional] 

## Example

```python
from tele_rest.models.inline_query_result_document import InlineQueryResultDocument

# TODO update the JSON string below
json = "{}"
# create an instance of InlineQueryResultDocument from a JSON string
inline_query_result_document_instance = InlineQueryResultDocument.from_json(json)
# print the JSON string representation of the object
print(InlineQueryResultDocument.to_json())

# convert the object into a dict
inline_query_result_document_dict = inline_query_result_document_instance.to_dict()
# create an instance of InlineQueryResultDocument from a dict
inline_query_result_document_from_dict = InlineQueryResultDocument.from_dict(inline_query_result_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


