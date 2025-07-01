# TransactionPartnerUser

Describes a transaction with a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the transaction partner, always “user” | [default to 'user']
**transaction_type** | **str** | Type of the transaction, currently one of “invoice\\_payment” for payments via invoices, “paid\\_media\\_payment” for payments for paid media, “gift\\_purchase” for gifts sent by the bot, “premium\\_purchase” for Telegram Premium subscriptions gifted by the bot, “business\\_account\\_transfer” for direct transfers from managed business accounts | 
**user** | [**User**](User.md) |  | 
**affiliate** | [**AffiliateInfo**](AffiliateInfo.md) |  | [optional] 
**invoice_payload** | **str** | *Optional*. Bot-specified invoice payload. Can be available only for “invoice\\_payment” transactions. | [optional] 
**subscription_period** | **int** | *Optional*. The duration of the paid subscription. Can be available only for “invoice\\_payment” transactions. | [optional] 
**paid_media** | [**List[PaidMedia]**](PaidMedia.md) | *Optional*. Information about the paid media bought by the user; for “paid\\_media\\_payment” transactions only | [optional] 
**paid_media_payload** | **str** | *Optional*. Bot-specified paid media payload. Can be available only for “paid\\_media\\_payment” transactions. | [optional] 
**gift** | [**Gift**](Gift.md) |  | [optional] 
**premium_subscription_duration** | **int** | *Optional*. Number of months the gifted Telegram Premium subscription will be active for; for “premium\\_purchase” transactions only | [optional] 

## Example

```python
from tele_rest.models.transaction_partner_user import TransactionPartnerUser

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPartnerUser from a JSON string
transaction_partner_user_instance = TransactionPartnerUser.from_json(json)
# print the JSON string representation of the object
print(TransactionPartnerUser.to_json())

# convert the object into a dict
transaction_partner_user_dict = transaction_partner_user_instance.to_dict()
# create an instance of TransactionPartnerUser from a dict
transaction_partner_user_from_dict = TransactionPartnerUser.from_dict(transaction_partner_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


