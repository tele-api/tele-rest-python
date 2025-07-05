# GetBusinessAccountStarBalanceRequest

Request parameters for getBusinessAccountStarBalance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 

## Example

```python
from tele_rest.models.get_business_account_star_balance_request import GetBusinessAccountStarBalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetBusinessAccountStarBalanceRequest from a JSON string
get_business_account_star_balance_request_instance = GetBusinessAccountStarBalanceRequest.from_json(json)
# print the JSON string representation of the object
print(GetBusinessAccountStarBalanceRequest.to_json())

# convert the object into a dict
get_business_account_star_balance_request_dict = get_business_account_star_balance_request_instance.to_dict()
# create an instance of GetBusinessAccountStarBalanceRequest from a dict
get_business_account_star_balance_request_from_dict = GetBusinessAccountStarBalanceRequest.from_dict(get_business_account_star_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


