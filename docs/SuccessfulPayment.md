# SuccessfulPayment

This object contains basic information about a successful payment. Note that if the buyer initiates a chargeback with the relevant payment provider following this transaction, the funds may be debited from your balance. This is outside of Telegram's control.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90) | 
**total_amount** | **int** | Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of &#x60;US$ 1.45&#x60; pass &#x60;amount &#x3D; 145&#x60;. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). | 
**invoice_payload** | **str** | Bot-specified invoice payload | 
**subscription_expiration_date** | **int** | *Optional*. Expiration date of the subscription, in Unix time; for recurring payments only | [optional] 
**is_recurring** | **bool** | *Optional*. *True*, if the payment is a recurring payment for a subscription | [optional] [default to True]
**is_first_recurring** | **bool** | *Optional*. *True*, if the payment is the first payment for a subscription | [optional] [default to True]
**shipping_option_id** | **str** | *Optional*. Identifier of the shipping option chosen by the user | [optional] 
**order_info** | [**OrderInfo**](OrderInfo.md) |  | [optional] 
**telegram_payment_charge_id** | **str** | Telegram payment identifier | 
**provider_payment_charge_id** | **str** | Provider payment identifier | 

## Example

```python
from tele_rest.models.successful_payment import SuccessfulPayment

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessfulPayment from a JSON string
successful_payment_instance = SuccessfulPayment.from_json(json)
# print the JSON string representation of the object
print(SuccessfulPayment.to_json())

# convert the object into a dict
successful_payment_dict = successful_payment_instance.to_dict()
# create an instance of SuccessfulPayment from a dict
successful_payment_from_dict = SuccessfulPayment.from_dict(successful_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


