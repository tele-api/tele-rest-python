# SetStickerSetThumbnailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_sticker_set_thumbnail_response import SetStickerSetThumbnailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetStickerSetThumbnailResponse from a JSON string
set_sticker_set_thumbnail_response_instance = SetStickerSetThumbnailResponse.from_json(json)
# print the JSON string representation of the object
print(SetStickerSetThumbnailResponse.to_json())

# convert the object into a dict
set_sticker_set_thumbnail_response_dict = set_sticker_set_thumbnail_response_instance.to_dict()
# create an instance of SetStickerSetThumbnailResponse from a dict
set_sticker_set_thumbnail_response_from_dict = SetStickerSetThumbnailResponse.from_dict(set_sticker_set_thumbnail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


