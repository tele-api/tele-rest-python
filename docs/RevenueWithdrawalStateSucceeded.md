# RevenueWithdrawalStateSucceeded

The withdrawal succeeded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the state, always “succeeded” | [default to 'succeeded']
**var_date** | **int** | Date the withdrawal was completed in Unix time | 
**url** | **str** | An HTTPS URL that can be used to see transaction details | 

## Example

```python
from tele_rest.models.revenue_withdrawal_state_succeeded import RevenueWithdrawalStateSucceeded

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueWithdrawalStateSucceeded from a JSON string
revenue_withdrawal_state_succeeded_instance = RevenueWithdrawalStateSucceeded.from_json(json)
# print the JSON string representation of the object
print(RevenueWithdrawalStateSucceeded.to_json())

# convert the object into a dict
revenue_withdrawal_state_succeeded_dict = revenue_withdrawal_state_succeeded_instance.to_dict()
# create an instance of RevenueWithdrawalStateSucceeded from a dict
revenue_withdrawal_state_succeeded_from_dict = RevenueWithdrawalStateSucceeded.from_dict(revenue_withdrawal_state_succeeded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


