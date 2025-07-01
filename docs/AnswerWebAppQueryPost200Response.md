# AnswerWebAppQueryPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**SentWebAppMessage**](SentWebAppMessage.md) |  | 

## Example

```python
from tele_rest.models.answer_web_app_query_post200_response import AnswerWebAppQueryPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerWebAppQueryPost200Response from a JSON string
answer_web_app_query_post200_response_instance = AnswerWebAppQueryPost200Response.from_json(json)
# print the JSON string representation of the object
print(AnswerWebAppQueryPost200Response.to_json())

# convert the object into a dict
answer_web_app_query_post200_response_dict = answer_web_app_query_post200_response_instance.to_dict()
# create an instance of AnswerWebAppQueryPost200Response from a dict
answer_web_app_query_post200_response_from_dict = AnswerWebAppQueryPost200Response.from_dict(answer_web_app_query_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


