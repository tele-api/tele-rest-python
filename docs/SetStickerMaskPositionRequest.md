# SetStickerMaskPositionRequest

Request parameters for setStickerMaskPosition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticker** | **str** | File identifier of the sticker | 
**mask_position** | [**MaskPosition**](MaskPosition.md) |  | [optional] 

## Example

```python
from tele_rest.models.set_sticker_mask_position_request import SetStickerMaskPositionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetStickerMaskPositionRequest from a JSON string
set_sticker_mask_position_request_instance = SetStickerMaskPositionRequest.from_json(json)
# print the JSON string representation of the object
print(SetStickerMaskPositionRequest.to_json())

# convert the object into a dict
set_sticker_mask_position_request_dict = set_sticker_mask_position_request_instance.to_dict()
# create an instance of SetStickerMaskPositionRequest from a dict
set_sticker_mask_position_request_from_dict = SetStickerMaskPositionRequest.from_dict(set_sticker_mask_position_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


