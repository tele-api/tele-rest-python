# AnswerWebAppQueryRequest

Request parameters for answerWebAppQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_app_query_id** | **str** | Unique identifier for the query to be answered | 
**result** | [**InlineQueryResult**](InlineQueryResult.md) |  | 

## Example

```python
from tele_rest.models.answer_web_app_query_request import AnswerWebAppQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerWebAppQueryRequest from a JSON string
answer_web_app_query_request_instance = AnswerWebAppQueryRequest.from_json(json)
# print the JSON string representation of the object
print(AnswerWebAppQueryRequest.to_json())

# convert the object into a dict
answer_web_app_query_request_dict = answer_web_app_query_request_instance.to_dict()
# create an instance of AnswerWebAppQueryRequest from a dict
answer_web_app_query_request_from_dict = AnswerWebAppQueryRequest.from_dict(answer_web_app_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


