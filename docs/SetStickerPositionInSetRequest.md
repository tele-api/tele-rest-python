# SetStickerPositionInSetRequest

Request parameters for setStickerPositionInSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticker** | **str** | File identifier of the sticker | 
**position** | **int** | New sticker position in the set, zero-based | 

## Example

```python
from tele_rest.models.set_sticker_position_in_set_request import SetStickerPositionInSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetStickerPositionInSetRequest from a JSON string
set_sticker_position_in_set_request_instance = SetStickerPositionInSetRequest.from_json(json)
# print the JSON string representation of the object
print(SetStickerPositionInSetRequest.to_json())

# convert the object into a dict
set_sticker_position_in_set_request_dict = set_sticker_position_in_set_request_instance.to_dict()
# create an instance of SetStickerPositionInSetRequest from a dict
set_sticker_position_in_set_request_from_dict = SetStickerPositionInSetRequest.from_dict(set_sticker_position_in_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


