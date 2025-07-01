# TransactionPartnerFragment

Describes a withdrawal transaction with Fragment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the transaction partner, always “fragment” | [default to 'fragment']
**withdrawal_state** | [**RevenueWithdrawalState**](RevenueWithdrawalState.md) |  | [optional] 

## Example

```python
from tele_rest.models.transaction_partner_fragment import TransactionPartnerFragment

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPartnerFragment from a JSON string
transaction_partner_fragment_instance = TransactionPartnerFragment.from_json(json)
# print the JSON string representation of the object
print(TransactionPartnerFragment.to_json())

# convert the object into a dict
transaction_partner_fragment_dict = transaction_partner_fragment_instance.to_dict()
# create an instance of TransactionPartnerFragment from a dict
transaction_partner_fragment_from_dict = TransactionPartnerFragment.from_dict(transaction_partner_fragment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


