# TransferGiftRequest

Request parameters for transferGift

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**owned_gift_id** | **str** | Unique identifier of the regular gift that should be transferred | 
**new_owner_chat_id** | **int** | Unique identifier of the chat which will own the gift. The chat must be active in the last 24 hours. | 
**star_count** | **int** | The amount of Telegram Stars that will be paid for the transfer from the business account balance. If positive, then the *can\\_transfer\\_stars* business bot right is required. | [optional] 

## Example

```python
from tele_rest.models.transfer_gift_request import TransferGiftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferGiftRequest from a JSON string
transfer_gift_request_instance = TransferGiftRequest.from_json(json)
# print the JSON string representation of the object
print(TransferGiftRequest.to_json())

# convert the object into a dict
transfer_gift_request_dict = transfer_gift_request_instance.to_dict()
# create an instance of TransferGiftRequest from a dict
transfer_gift_request_from_dict = TransferGiftRequest.from_dict(transfer_gift_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


