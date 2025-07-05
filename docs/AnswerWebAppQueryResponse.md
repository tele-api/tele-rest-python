# AnswerWebAppQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**SentWebAppMessage**](SentWebAppMessage.md) |  | 

## Example

```python
from tele_rest.models.answer_web_app_query_response import AnswerWebAppQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerWebAppQueryResponse from a JSON string
answer_web_app_query_response_instance = AnswerWebAppQueryResponse.from_json(json)
# print the JSON string representation of the object
print(AnswerWebAppQueryResponse.to_json())

# convert the object into a dict
answer_web_app_query_response_dict = answer_web_app_query_response_instance.to_dict()
# create an instance of AnswerWebAppQueryResponse from a dict
answer_web_app_query_response_from_dict = AnswerWebAppQueryResponse.from_dict(answer_web_app_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


