# GetStarTransactionsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Number of transactions to skip in the response | [optional] 
**limit** | **int** | The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100. | [optional] [default to 100]

## Example

```python
from tele_rest.models.get_star_transactions_post_request import GetStarTransactionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStarTransactionsPostRequest from a JSON string
get_star_transactions_post_request_instance = GetStarTransactionsPostRequest.from_json(json)
# print the JSON string representation of the object
print(GetStarTransactionsPostRequest.to_json())

# convert the object into a dict
get_star_transactions_post_request_dict = get_star_transactions_post_request_instance.to_dict()
# create an instance of GetStarTransactionsPostRequest from a dict
get_star_transactions_post_request_from_dict = GetStarTransactionsPostRequest.from_dict(get_star_transactions_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


