# RevenueWithdrawalStatePending

The withdrawal is in progress.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the state, always “pending” | [default to 'pending']

## Example

```python
from tele_rest.models.revenue_withdrawal_state_pending import RevenueWithdrawalStatePending

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueWithdrawalStatePending from a JSON string
revenue_withdrawal_state_pending_instance = RevenueWithdrawalStatePending.from_json(json)
# print the JSON string representation of the object
print(RevenueWithdrawalStatePending.to_json())

# convert the object into a dict
revenue_withdrawal_state_pending_dict = revenue_withdrawal_state_pending_instance.to_dict()
# create an instance of RevenueWithdrawalStatePending from a dict
revenue_withdrawal_state_pending_from_dict = RevenueWithdrawalStatePending.from_dict(revenue_withdrawal_state_pending_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


