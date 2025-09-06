# SuggestedPostPaid

Describes a service message about a successful payment for a suggested post.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggested_post_message** | [**Message**](Message.md) |  | [optional] 
**currency** | **str** | Currency in which the payment was made. Currently, one of “XTR” for Telegram Stars or “TON” for toncoins | 
**amount** | **int** | *Optional*. The amount of the currency that was received by the channel in nanotoncoins; for payments in toncoins only | [optional] 
**star_amount** | [**StarAmount**](StarAmount.md) |  | [optional] 

## Example

```python
from tele_rest.models.suggested_post_paid import SuggestedPostPaid

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedPostPaid from a JSON string
suggested_post_paid_instance = SuggestedPostPaid.from_json(json)
# print the JSON string representation of the object
print(SuggestedPostPaid.to_json())

# convert the object into a dict
suggested_post_paid_dict = suggested_post_paid_instance.to_dict()
# create an instance of SuggestedPostPaid from a dict
suggested_post_paid_from_dict = SuggestedPostPaid.from_dict(suggested_post_paid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


