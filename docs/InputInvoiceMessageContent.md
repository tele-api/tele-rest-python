# InputInvoiceMessageContent

Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of an invoice message to be sent as the result of an inline query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Product name, 1-32 characters | 
**description** | **str** | Product description, 1-255 characters | 
**payload** | **str** | Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes. | 
**provider_token** | **str** | *Optional*. Payment provider token, obtained via [@BotFather](https://t.me/botfather). Pass an empty string for payments in [Telegram Stars](https://t.me/BotNews/90). | [optional] 
**currency** | **str** | Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies). Pass “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90). | 
**prices** | [**List[LabeledPrice]**](LabeledPrice.md) | Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in [Telegram Stars](https://t.me/BotNews/90). | 
**max_tip_amount** | **int** | *Optional*. The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of &#x60;US$ 1.45&#x60; pass &#x60;max_tip_amount &#x3D; 145&#x60;. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in [Telegram Stars](https://t.me/BotNews/90). | [optional] [default to 0]
**suggested_tip_amounts** | **List[int]** | *Optional*. A JSON-serialized array of suggested amounts of tip in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max\\_tip\\_amount*. | [optional] 
**provider_data** | **str** | *Optional*. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider. | [optional] 
**photo_url** | **str** | *Optional*. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. | [optional] 
**photo_size** | **int** | *Optional*. Photo size in bytes | [optional] 
**photo_width** | **int** | *Optional*. Photo width | [optional] 
**photo_height** | **int** | *Optional*. Photo height | [optional] 
**need_name** | **bool** | *Optional*. Pass *True* if you require the user&#39;s full name to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). | [optional] 
**need_phone_number** | **bool** | *Optional*. Pass *True* if you require the user&#39;s phone number to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). | [optional] 
**need_email** | **bool** | *Optional*. Pass *True* if you require the user&#39;s email address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). | [optional] 
**need_shipping_address** | **bool** | *Optional*. Pass *True* if you require the user&#39;s shipping address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). | [optional] 
**send_phone_number_to_provider** | **bool** | *Optional*. Pass *True* if the user&#39;s phone number should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). | [optional] 
**send_email_to_provider** | **bool** | *Optional*. Pass *True* if the user&#39;s email address should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). | [optional] 
**is_flexible** | **bool** | *Optional*. Pass *True* if the final price depends on the shipping method. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). | [optional] 

## Example

```python
from tele_rest.models.input_invoice_message_content import InputInvoiceMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of InputInvoiceMessageContent from a JSON string
input_invoice_message_content_instance = InputInvoiceMessageContent.from_json(json)
# print the JSON string representation of the object
print(InputInvoiceMessageContent.to_json())

# convert the object into a dict
input_invoice_message_content_dict = input_invoice_message_content_instance.to_dict()
# create an instance of InputInvoiceMessageContent from a dict
input_invoice_message_content_from_dict = InputInvoiceMessageContent.from_dict(input_invoice_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


