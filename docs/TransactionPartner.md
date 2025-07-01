# TransactionPartner

This object describes the source of a transaction, or its recipient for outgoing transactions. Currently, it can be one of  * [TransactionPartnerUser](https://core.telegram.org/bots/api/#transactionpartneruser) * [TransactionPartnerChat](https://core.telegram.org/bots/api/#transactionpartnerchat) * [TransactionPartnerAffiliateProgram](https://core.telegram.org/bots/api/#transactionpartneraffiliateprogram) * [TransactionPartnerFragment](https://core.telegram.org/bots/api/#transactionpartnerfragment) * [TransactionPartnerTelegramAds](https://core.telegram.org/bots/api/#transactionpartnertelegramads) * [TransactionPartnerTelegramApi](https://core.telegram.org/bots/api/#transactionpartnertelegramapi) * [TransactionPartnerOther](https://core.telegram.org/bots/api/#transactionpartnerother)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the transaction partner, always “other” | [default to 'other']
**transaction_type** | **str** | Type of the transaction, currently one of “invoice\\_payment” for payments via invoices, “paid\\_media\\_payment” for payments for paid media, “gift\\_purchase” for gifts sent by the bot, “premium\\_purchase” for Telegram Premium subscriptions gifted by the bot, “business\\_account\\_transfer” for direct transfers from managed business accounts | 
**user** | [**User**](User.md) |  | 
**affiliate** | [**AffiliateInfo**](AffiliateInfo.md) |  | [optional] 
**invoice_payload** | **str** | *Optional*. Bot-specified invoice payload. Can be available only for “invoice\\_payment” transactions. | [optional] 
**subscription_period** | **int** | *Optional*. The duration of the paid subscription. Can be available only for “invoice\\_payment” transactions. | [optional] 
**paid_media** | [**List[PaidMedia]**](PaidMedia.md) | *Optional*. Information about the paid media bought by the user; for “paid\\_media\\_payment” transactions only | [optional] 
**paid_media_payload** | **str** | *Optional*. Bot-specified paid media payload. Can be available only for “paid\\_media\\_payment” transactions. | [optional] 
**gift** | [**Gift**](Gift.md) |  | [optional] 
**premium_subscription_duration** | **int** | *Optional*. Number of months the gifted Telegram Premium subscription will be active for; for “premium\\_purchase” transactions only | [optional] 
**chat** | [**Chat**](Chat.md) |  | 
**sponsor_user** | [**User**](User.md) |  | [optional] 
**commission_per_mille** | **int** | The number of Telegram Stars received by the bot for each 1000 Telegram Stars received by the affiliate program sponsor from referred users | 
**withdrawal_state** | [**RevenueWithdrawalState**](RevenueWithdrawalState.md) |  | [optional] 
**request_count** | **int** | The number of successful requests that exceeded regular limits and were therefore billed | 

## Example

```python
from tele_rest.models.transaction_partner import TransactionPartner

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPartner from a JSON string
transaction_partner_instance = TransactionPartner.from_json(json)
# print the JSON string representation of the object
print(TransactionPartner.to_json())

# convert the object into a dict
transaction_partner_dict = transaction_partner_instance.to_dict()
# create an instance of TransactionPartner from a dict
transaction_partner_from_dict = TransactionPartner.from_dict(transaction_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


