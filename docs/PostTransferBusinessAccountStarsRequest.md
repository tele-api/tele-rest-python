# PostTransferBusinessAccountStarsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**star_count** | **int** | Number of Telegram Stars to transfer; 1-10000 | 

## Example

```python
from tele_rest.models.post_transfer_business_account_stars_request import PostTransferBusinessAccountStarsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTransferBusinessAccountStarsRequest from a JSON string
post_transfer_business_account_stars_request_instance = PostTransferBusinessAccountStarsRequest.from_json(json)
# print the JSON string representation of the object
print(PostTransferBusinessAccountStarsRequest.to_json())

# convert the object into a dict
post_transfer_business_account_stars_request_dict = post_transfer_business_account_stars_request_instance.to_dict()
# create an instance of PostTransferBusinessAccountStarsRequest from a dict
post_transfer_business_account_stars_request_from_dict = PostTransferBusinessAccountStarsRequest.from_dict(post_transfer_business_account_stars_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


