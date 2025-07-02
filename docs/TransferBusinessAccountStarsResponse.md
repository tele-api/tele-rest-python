# TransferBusinessAccountStarsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.transfer_business_account_stars_response import TransferBusinessAccountStarsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransferBusinessAccountStarsResponse from a JSON string
transfer_business_account_stars_response_instance = TransferBusinessAccountStarsResponse.from_json(json)
# print the JSON string representation of the object
print(TransferBusinessAccountStarsResponse.to_json())

# convert the object into a dict
transfer_business_account_stars_response_dict = transfer_business_account_stars_response_instance.to_dict()
# create an instance of TransferBusinessAccountStarsResponse from a dict
transfer_business_account_stars_response_from_dict = TransferBusinessAccountStarsResponse.from_dict(transfer_business_account_stars_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


