# PostTransferGiftRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**owned_gift_id** | **str** | Unique identifier of the regular gift that should be transferred | 
**new_owner_chat_id** | **int** | Unique identifier of the chat which will own the gift. The chat must be active in the last 24 hours. | 
**star_count** | **int** | The amount of Telegram Stars that will be paid for the transfer from the business account balance. If positive, then the *can\\_transfer\\_stars* business bot right is required. | [optional] 

## Example

```python
from tele_rest.models.post_transfer_gift_request import PostTransferGiftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTransferGiftRequest from a JSON string
post_transfer_gift_request_instance = PostTransferGiftRequest.from_json(json)
# print the JSON string representation of the object
print(PostTransferGiftRequest.to_json())

# convert the object into a dict
post_transfer_gift_request_dict = post_transfer_gift_request_instance.to_dict()
# create an instance of PostTransferGiftRequest from a dict
post_transfer_gift_request_from_dict = PostTransferGiftRequest.from_dict(post_transfer_gift_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


