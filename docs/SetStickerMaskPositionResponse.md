# SetStickerMaskPositionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_sticker_mask_position_response import SetStickerMaskPositionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetStickerMaskPositionResponse from a JSON string
set_sticker_mask_position_response_instance = SetStickerMaskPositionResponse.from_json(json)
# print the JSON string representation of the object
print(SetStickerMaskPositionResponse.to_json())

# convert the object into a dict
set_sticker_mask_position_response_dict = set_sticker_mask_position_response_instance.to_dict()
# create an instance of SetStickerMaskPositionResponse from a dict
set_sticker_mask_position_response_from_dict = SetStickerMaskPositionResponse.from_dict(set_sticker_mask_position_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


