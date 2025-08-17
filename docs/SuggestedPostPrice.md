# SuggestedPostPrice

Desribes price of a suggested post.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency in which the post will be paid. Currently, must be one of “XTR” for Telegram Stars or “TON” for toncoins | 
**amount** | **int** | The amount of the currency that will be paid for the post in the *smallest units* of the currency, i.e. Telegram Stars or nanotoncoins. Currently, price in Telegram Stars must be between 5 and 100000, and price in nanotoncoins must be between 10000000 and 10000000000000. | 

## Example

```python
from tele_rest.models.suggested_post_price import SuggestedPostPrice

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedPostPrice from a JSON string
suggested_post_price_instance = SuggestedPostPrice.from_json(json)
# print the JSON string representation of the object
print(SuggestedPostPrice.to_json())

# convert the object into a dict
suggested_post_price_dict = suggested_post_price_instance.to_dict()
# create an instance of SuggestedPostPrice from a dict
suggested_post_price_from_dict = SuggestedPostPrice.from_dict(suggested_post_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


