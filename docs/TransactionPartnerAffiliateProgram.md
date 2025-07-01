# TransactionPartnerAffiliateProgram

Describes the affiliate program that issued the affiliate commission received via this transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the transaction partner, always “affiliate\\_program” | [default to 'affiliate_program']
**sponsor_user** | [**User**](User.md) |  | [optional] 
**commission_per_mille** | **int** | The number of Telegram Stars received by the bot for each 1000 Telegram Stars received by the affiliate program sponsor from referred users | 

## Example

```python
from tele_rest.models.transaction_partner_affiliate_program import TransactionPartnerAffiliateProgram

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPartnerAffiliateProgram from a JSON string
transaction_partner_affiliate_program_instance = TransactionPartnerAffiliateProgram.from_json(json)
# print the JSON string representation of the object
print(TransactionPartnerAffiliateProgram.to_json())

# convert the object into a dict
transaction_partner_affiliate_program_dict = transaction_partner_affiliate_program_instance.to_dict()
# create an instance of TransactionPartnerAffiliateProgram from a dict
transaction_partner_affiliate_program_from_dict = TransactionPartnerAffiliateProgram.from_dict(transaction_partner_affiliate_program_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


