# RefundedPayment

This object contains basic information about a refunded payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90). Currently, always “XTR” | [default to 'XTR']
**total_amount** | **int** | Total refunded price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of &#x60;US$ 1.45&#x60;, &#x60;total_amount &#x3D; 145&#x60;. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). | 
**invoice_payload** | **str** | Bot-specified invoice payload | 
**telegram_payment_charge_id** | **str** | Telegram payment identifier | 
**provider_payment_charge_id** | **str** | *Optional*. Provider payment identifier | [optional] 

## Example

```python
from tele_rest.models.refunded_payment import RefundedPayment

# TODO update the JSON string below
json = "{}"
# create an instance of RefundedPayment from a JSON string
refunded_payment_instance = RefundedPayment.from_json(json)
# print the JSON string representation of the object
print(RefundedPayment.to_json())

# convert the object into a dict
refunded_payment_dict = refunded_payment_instance.to_dict()
# create an instance of RefundedPayment from a dict
refunded_payment_from_dict = RefundedPayment.from_dict(refunded_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


