# StarTransactions

Contains a list of Telegram Star transactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[StarTransaction]**](StarTransaction.md) | The list of transactions | 

## Example

```python
from tele_rest.models.star_transactions import StarTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of StarTransactions from a JSON string
star_transactions_instance = StarTransactions.from_json(json)
# print the JSON string representation of the object
print(StarTransactions.to_json())

# convert the object into a dict
star_transactions_dict = star_transactions_instance.to_dict()
# create an instance of StarTransactions from a dict
star_transactions_from_dict = StarTransactions.from_dict(star_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


