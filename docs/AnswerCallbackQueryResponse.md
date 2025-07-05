# AnswerCallbackQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.answer_callback_query_response import AnswerCallbackQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerCallbackQueryResponse from a JSON string
answer_callback_query_response_instance = AnswerCallbackQueryResponse.from_json(json)
# print the JSON string representation of the object
print(AnswerCallbackQueryResponse.to_json())

# convert the object into a dict
answer_callback_query_response_dict = answer_callback_query_response_instance.to_dict()
# create an instance of AnswerCallbackQueryResponse from a dict
answer_callback_query_response_from_dict = AnswerCallbackQueryResponse.from_dict(answer_callback_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


