# GetStarTransactionsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**StarTransactions**](StarTransactions.md) |  | 

## Example

```python
from tele_rest.models.get_star_transactions_post200_response import GetStarTransactionsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStarTransactionsPost200Response from a JSON string
get_star_transactions_post200_response_instance = GetStarTransactionsPost200Response.from_json(json)
# print the JSON string representation of the object
print(GetStarTransactionsPost200Response.to_json())

# convert the object into a dict
get_star_transactions_post200_response_dict = get_star_transactions_post200_response_instance.to_dict()
# create an instance of GetStarTransactionsPost200Response from a dict
get_star_transactions_post200_response_from_dict = GetStarTransactionsPost200Response.from_dict(get_star_transactions_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


