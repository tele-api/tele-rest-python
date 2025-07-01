# TransactionPartnerOther

Describes a transaction with an unknown source or recipient.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the transaction partner, always “other” | [default to 'other']

## Example

```python
from tele_rest.models.transaction_partner_other import TransactionPartnerOther

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPartnerOther from a JSON string
transaction_partner_other_instance = TransactionPartnerOther.from_json(json)
# print the JSON string representation of the object
print(TransactionPartnerOther.to_json())

# convert the object into a dict
transaction_partner_other_dict = transaction_partner_other_instance.to_dict()
# create an instance of TransactionPartnerOther from a dict
transaction_partner_other_from_dict = TransactionPartnerOther.from_dict(transaction_partner_other_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


