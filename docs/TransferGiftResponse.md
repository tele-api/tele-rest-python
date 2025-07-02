# TransferGiftResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.transfer_gift_response import TransferGiftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransferGiftResponse from a JSON string
transfer_gift_response_instance = TransferGiftResponse.from_json(json)
# print the JSON string representation of the object
print(TransferGiftResponse.to_json())

# convert the object into a dict
transfer_gift_response_dict = transfer_gift_response_instance.to_dict()
# create an instance of TransferGiftResponse from a dict
transfer_gift_response_from_dict = TransferGiftResponse.from_dict(transfer_gift_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


