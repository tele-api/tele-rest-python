# GetMyStarBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**StarAmount**](StarAmount.md) |  | 

## Example

```python
from tele_rest.models.get_my_star_balance_response import GetMyStarBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyStarBalanceResponse from a JSON string
get_my_star_balance_response_instance = GetMyStarBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(GetMyStarBalanceResponse.to_json())

# convert the object into a dict
get_my_star_balance_response_dict = get_my_star_balance_response_instance.to_dict()
# create an instance of GetMyStarBalanceResponse from a dict
get_my_star_balance_response_from_dict = GetMyStarBalanceResponse.from_dict(get_my_star_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


