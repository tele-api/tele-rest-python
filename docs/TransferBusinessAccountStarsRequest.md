# TransferBusinessAccountStarsRequest

Request parameters for transferBusinessAccountStars

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**star_count** | **int** | Number of Telegram Stars to transfer; 1-10000 | 

## Example

```python
from tele_rest.models.transfer_business_account_stars_request import TransferBusinessAccountStarsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferBusinessAccountStarsRequest from a JSON string
transfer_business_account_stars_request_instance = TransferBusinessAccountStarsRequest.from_json(json)
# print the JSON string representation of the object
print(TransferBusinessAccountStarsRequest.to_json())

# convert the object into a dict
transfer_business_account_stars_request_dict = transfer_business_account_stars_request_instance.to_dict()
# create an instance of TransferBusinessAccountStarsRequest from a dict
transfer_business_account_stars_request_from_dict = TransferBusinessAccountStarsRequest.from_dict(transfer_business_account_stars_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


