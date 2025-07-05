# GetBusinessAccountStarBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**StarAmount**](StarAmount.md) |  | 

## Example

```python
from tele_rest.models.get_business_account_star_balance_response import GetBusinessAccountStarBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBusinessAccountStarBalanceResponse from a JSON string
get_business_account_star_balance_response_instance = GetBusinessAccountStarBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(GetBusinessAccountStarBalanceResponse.to_json())

# convert the object into a dict
get_business_account_star_balance_response_dict = get_business_account_star_balance_response_instance.to_dict()
# create an instance of GetBusinessAccountStarBalanceResponse from a dict
get_business_account_star_balance_response_from_dict = GetBusinessAccountStarBalanceResponse.from_dict(get_business_account_star_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


