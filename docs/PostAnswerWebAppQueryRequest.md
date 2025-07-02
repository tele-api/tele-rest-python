# PostAnswerWebAppQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_app_query_id** | **str** | Unique identifier for the query to be answered | 
**result** | [**InlineQueryResult**](InlineQueryResult.md) |  | 

## Example

```python
from tele_rest.models.post_answer_web_app_query_request import PostAnswerWebAppQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAnswerWebAppQueryRequest from a JSON string
post_answer_web_app_query_request_instance = PostAnswerWebAppQueryRequest.from_json(json)
# print the JSON string representation of the object
print(PostAnswerWebAppQueryRequest.to_json())

# convert the object into a dict
post_answer_web_app_query_request_dict = post_answer_web_app_query_request_instance.to_dict()
# create an instance of PostAnswerWebAppQueryRequest from a dict
post_answer_web_app_query_request_from_dict = PostAnswerWebAppQueryRequest.from_dict(post_answer_web_app_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


