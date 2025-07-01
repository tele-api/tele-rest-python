# TransactionPartnerTelegramAds

Describes a withdrawal transaction to the Telegram Ads platform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the transaction partner, always “telegram\\_ads” | [default to 'telegram_ads']

## Example

```python
from tele_rest.models.transaction_partner_telegram_ads import TransactionPartnerTelegramAds

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPartnerTelegramAds from a JSON string
transaction_partner_telegram_ads_instance = TransactionPartnerTelegramAds.from_json(json)
# print the JSON string representation of the object
print(TransactionPartnerTelegramAds.to_json())

# convert the object into a dict
transaction_partner_telegram_ads_dict = transaction_partner_telegram_ads_instance.to_dict()
# create an instance of TransactionPartnerTelegramAds from a dict
transaction_partner_telegram_ads_from_dict = TransactionPartnerTelegramAds.from_dict(transaction_partner_telegram_ads_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


