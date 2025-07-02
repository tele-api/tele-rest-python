# PostSetStickerMaskPositionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticker** | **str** | File identifier of the sticker | 
**mask_position** | [**MaskPosition**](MaskPosition.md) |  | [optional] 

## Example

```python
from tele_rest.models.post_set_sticker_mask_position_request import PostSetStickerMaskPositionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetStickerMaskPositionRequest from a JSON string
post_set_sticker_mask_position_request_instance = PostSetStickerMaskPositionRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetStickerMaskPositionRequest.to_json())

# convert the object into a dict
post_set_sticker_mask_position_request_dict = post_set_sticker_mask_position_request_instance.to_dict()
# create an instance of PostSetStickerMaskPositionRequest from a dict
post_set_sticker_mask_position_request_from_dict = PostSetStickerMaskPositionRequest.from_dict(post_set_sticker_mask_position_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


