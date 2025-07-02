# AnswerShippingQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.answer_shipping_query_response import AnswerShippingQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerShippingQueryResponse from a JSON string
answer_shipping_query_response_instance = AnswerShippingQueryResponse.from_json(json)
# print the JSON string representation of the object
print(AnswerShippingQueryResponse.to_json())

# convert the object into a dict
answer_shipping_query_response_dict = answer_shipping_query_response_instance.to_dict()
# create an instance of AnswerShippingQueryResponse from a dict
answer_shipping_query_response_from_dict = AnswerShippingQueryResponse.from_dict(answer_shipping_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


