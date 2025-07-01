# InlineQueryResultArticle

Represents a link to an article or web page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the result, must be *article* | [default to 'article']
**id** | **str** | Unique identifier for this result, 1-64 Bytes | 
**title** | **str** | Title of the result | 
**input_message_content** | [**InputMessageContent**](InputMessageContent.md) |  | 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**url** | **str** | *Optional*. URL of the result | [optional] 
**description** | **str** | *Optional*. Short description of the result | [optional] 
**thumbnail_url** | **str** | *Optional*. Url of the thumbnail for the result | [optional] 
**thumbnail_width** | **int** | *Optional*. Thumbnail width | [optional] 
**thumbnail_height** | **int** | *Optional*. Thumbnail height | [optional] 

## Example

```python
from tele_rest.models.inline_query_result_article import InlineQueryResultArticle

# TODO update the JSON string below
json = "{}"
# create an instance of InlineQueryResultArticle from a JSON string
inline_query_result_article_instance = InlineQueryResultArticle.from_json(json)
# print the JSON string representation of the object
print(InlineQueryResultArticle.to_json())

# convert the object into a dict
inline_query_result_article_dict = inline_query_result_article_instance.to_dict()
# create an instance of InlineQueryResultArticle from a dict
inline_query_result_article_from_dict = InlineQueryResultArticle.from_dict(inline_query_result_article_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


