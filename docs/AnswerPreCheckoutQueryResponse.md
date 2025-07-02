# AnswerPreCheckoutQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.answer_pre_checkout_query_response import AnswerPreCheckoutQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerPreCheckoutQueryResponse from a JSON string
answer_pre_checkout_query_response_instance = AnswerPreCheckoutQueryResponse.from_json(json)
# print the JSON string representation of the object
print(AnswerPreCheckoutQueryResponse.to_json())

# convert the object into a dict
answer_pre_checkout_query_response_dict = answer_pre_checkout_query_response_instance.to_dict()
# create an instance of AnswerPreCheckoutQueryResponse from a dict
answer_pre_checkout_query_response_from_dict = AnswerPreCheckoutQueryResponse.from_dict(answer_pre_checkout_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


