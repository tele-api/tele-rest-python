# PostGetStarTransactionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Number of transactions to skip in the response | [optional] 
**limit** | **int** | The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100. | [optional] [default to 100]

## Example

```python
from tele_rest.models.post_get_star_transactions_request import PostGetStarTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetStarTransactionsRequest from a JSON string
post_get_star_transactions_request_instance = PostGetStarTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(PostGetStarTransactionsRequest.to_json())

# convert the object into a dict
post_get_star_transactions_request_dict = post_get_star_transactions_request_instance.to_dict()
# create an instance of PostGetStarTransactionsRequest from a dict
post_get_star_transactions_request_from_dict = PostGetStarTransactionsRequest.from_dict(post_get_star_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


