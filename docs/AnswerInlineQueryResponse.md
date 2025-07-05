# AnswerInlineQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.answer_inline_query_response import AnswerInlineQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerInlineQueryResponse from a JSON string
answer_inline_query_response_instance = AnswerInlineQueryResponse.from_json(json)
# print the JSON string representation of the object
print(AnswerInlineQueryResponse.to_json())

# convert the object into a dict
answer_inline_query_response_dict = answer_inline_query_response_instance.to_dict()
# create an instance of AnswerInlineQueryResponse from a dict
answer_inline_query_response_from_dict = AnswerInlineQueryResponse.from_dict(answer_inline_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


