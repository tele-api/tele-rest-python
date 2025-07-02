# GetStarTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**StarTransactions**](StarTransactions.md) |  | 

## Example

```python
from tele_rest.models.get_star_transactions_response import GetStarTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStarTransactionsResponse from a JSON string
get_star_transactions_response_instance = GetStarTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetStarTransactionsResponse.to_json())

# convert the object into a dict
get_star_transactions_response_dict = get_star_transactions_response_instance.to_dict()
# create an instance of GetStarTransactionsResponse from a dict
get_star_transactions_response_from_dict = GetStarTransactionsResponse.from_dict(get_star_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


