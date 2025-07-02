# PostAnswerInlineQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline_query_id** | **str** | Unique identifier for the answered query | 
**results** | [**List[InlineQueryResult]**](InlineQueryResult.md) | A JSON-serialized array of results for the inline query | 
**cache_time** | **int** | The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300. | [optional] [default to 300]
**is_personal** | **bool** | Pass *True* if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query. | [optional] 
**next_offset** | **str** | Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don&#39;t support pagination. Offset length can&#39;t exceed 64 bytes. | [optional] 
**button** | [**InlineQueryResultsButton**](InlineQueryResultsButton.md) |  | [optional] 

## Example

```python
from tele_rest.models.post_answer_inline_query_request import PostAnswerInlineQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAnswerInlineQueryRequest from a JSON string
post_answer_inline_query_request_instance = PostAnswerInlineQueryRequest.from_json(json)
# print the JSON string representation of the object
print(PostAnswerInlineQueryRequest.to_json())

# convert the object into a dict
post_answer_inline_query_request_dict = post_answer_inline_query_request_instance.to_dict()
# create an instance of PostAnswerInlineQueryRequest from a dict
post_answer_inline_query_request_from_dict = PostAnswerInlineQueryRequest.from_dict(post_answer_inline_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


