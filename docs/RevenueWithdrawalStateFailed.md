# RevenueWithdrawalStateFailed

The withdrawal failed and the transaction was refunded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the state, always “failed” | [default to 'failed']

## Example

```python
from tele_rest.models.revenue_withdrawal_state_failed import RevenueWithdrawalStateFailed

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueWithdrawalStateFailed from a JSON string
revenue_withdrawal_state_failed_instance = RevenueWithdrawalStateFailed.from_json(json)
# print the JSON string representation of the object
print(RevenueWithdrawalStateFailed.to_json())

# convert the object into a dict
revenue_withdrawal_state_failed_dict = revenue_withdrawal_state_failed_instance.to_dict()
# create an instance of RevenueWithdrawalStateFailed from a dict
revenue_withdrawal_state_failed_from_dict = RevenueWithdrawalStateFailed.from_dict(revenue_withdrawal_state_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


