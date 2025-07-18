# PreCheckoutQuery

This object contains information about an incoming pre-checkout query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique query identifier | 
**var_from** | [**User**](User.md) |  | 
**currency** | **str** | Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90) | 
**total_amount** | **int** | Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of &#x60;US$ 1.45&#x60; pass &#x60;amount &#x3D; 145&#x60;. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). | 
**invoice_payload** | **str** | Bot-specified invoice payload | 
**shipping_option_id** | **str** | *Optional*. Identifier of the shipping option chosen by the user | [optional] 
**order_info** | [**OrderInfo**](OrderInfo.md) |  | [optional] 

## Example

```python
from tele_rest.models.pre_checkout_query import PreCheckoutQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PreCheckoutQuery from a JSON string
pre_checkout_query_instance = PreCheckoutQuery.from_json(json)
# print the JSON string representation of the object
print(PreCheckoutQuery.to_json())

# convert the object into a dict
pre_checkout_query_dict = pre_checkout_query_instance.to_dict()
# create an instance of PreCheckoutQuery from a dict
pre_checkout_query_from_dict = PreCheckoutQuery.from_dict(pre_checkout_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


