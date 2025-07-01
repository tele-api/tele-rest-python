# TransferBusinessAccountStarsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**star_count** | **int** | Number of Telegram Stars to transfer; 1-10000 | 

## Example

```python
from tele_rest.models.transfer_business_account_stars_post_request import TransferBusinessAccountStarsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferBusinessAccountStarsPostRequest from a JSON string
transfer_business_account_stars_post_request_instance = TransferBusinessAccountStarsPostRequest.from_json(json)
# print the JSON string representation of the object
print(TransferBusinessAccountStarsPostRequest.to_json())

# convert the object into a dict
transfer_business_account_stars_post_request_dict = transfer_business_account_stars_post_request_instance.to_dict()
# create an instance of TransferBusinessAccountStarsPostRequest from a dict
transfer_business_account_stars_post_request_from_dict = TransferBusinessAccountStarsPostRequest.from_dict(transfer_business_account_stars_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


