# TransactionPartnerTelegramApi

Describes a transaction with payment for [paid broadcasting](https://core.telegram.org/bots/api/#paid-broadcasts).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the transaction partner, always “telegram\\_api” | [default to 'telegram_api']
**request_count** | **int** | The number of successful requests that exceeded regular limits and were therefore billed | 

## Example

```python
from tele_rest.models.transaction_partner_telegram_api import TransactionPartnerTelegramApi

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPartnerTelegramApi from a JSON string
transaction_partner_telegram_api_instance = TransactionPartnerTelegramApi.from_json(json)
# print the JSON string representation of the object
print(TransactionPartnerTelegramApi.to_json())

# convert the object into a dict
transaction_partner_telegram_api_dict = transaction_partner_telegram_api_instance.to_dict()
# create an instance of TransactionPartnerTelegramApi from a dict
transaction_partner_telegram_api_from_dict = TransactionPartnerTelegramApi.from_dict(transaction_partner_telegram_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


