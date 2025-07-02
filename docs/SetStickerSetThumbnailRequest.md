# SetStickerSetThumbnailRequest

Request parameters for setStickerSetThumbnail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sticker set name | 
**user_id** | **int** | User identifier of the sticker set owner | 
**thumbnail** | **str** |  | [optional] 
**format** | **str** | Format of the thumbnail, must be one of “static” for a **.WEBP** or **.PNG** image, “animated” for a **.TGS** animation, or “video” for a **.WEBM** video | 

## Example

```python
from tele_rest.models.set_sticker_set_thumbnail_request import SetStickerSetThumbnailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetStickerSetThumbnailRequest from a JSON string
set_sticker_set_thumbnail_request_instance = SetStickerSetThumbnailRequest.from_json(json)
# print the JSON string representation of the object
print(SetStickerSetThumbnailRequest.to_json())

# convert the object into a dict
set_sticker_set_thumbnail_request_dict = set_sticker_set_thumbnail_request_instance.to_dict()
# create an instance of SetStickerSetThumbnailRequest from a dict
set_sticker_set_thumbnail_request_from_dict = SetStickerSetThumbnailRequest.from_dict(set_sticker_set_thumbnail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


