# RevenueWithdrawalState

This object describes the state of a revenue withdrawal operation. Currently, it can be one of  * [RevenueWithdrawalStatePending](https://core.telegram.org/bots/api/#revenuewithdrawalstatepending) * [RevenueWithdrawalStateSucceeded](https://core.telegram.org/bots/api/#revenuewithdrawalstatesucceeded) * [RevenueWithdrawalStateFailed](https://core.telegram.org/bots/api/#revenuewithdrawalstatefailed)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the state, always “failed” | [default to 'failed']
**var_date** | **int** | Date the withdrawal was completed in Unix time | 
**url** | **str** | An HTTPS URL that can be used to see transaction details | 

## Example

```python
from tele_rest.models.revenue_withdrawal_state import RevenueWithdrawalState

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueWithdrawalState from a JSON string
revenue_withdrawal_state_instance = RevenueWithdrawalState.from_json(json)
# print the JSON string representation of the object
print(RevenueWithdrawalState.to_json())

# convert the object into a dict
revenue_withdrawal_state_dict = revenue_withdrawal_state_instance.to_dict()
# create an instance of RevenueWithdrawalState from a dict
revenue_withdrawal_state_from_dict = RevenueWithdrawalState.from_dict(revenue_withdrawal_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


