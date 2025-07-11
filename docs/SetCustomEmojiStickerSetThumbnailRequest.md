# SetCustomEmojiStickerSetThumbnailRequest

Request parameters for setCustomEmojiStickerSetThumbnail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sticker set name | 
**custom_emoji_id** | **str** | Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail. | [optional] 

## Example

```python
from tele_rest.models.set_custom_emoji_sticker_set_thumbnail_request import SetCustomEmojiStickerSetThumbnailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetCustomEmojiStickerSetThumbnailRequest from a JSON string
set_custom_emoji_sticker_set_thumbnail_request_instance = SetCustomEmojiStickerSetThumbnailRequest.from_json(json)
# print the JSON string representation of the object
print(SetCustomEmojiStickerSetThumbnailRequest.to_json())

# convert the object into a dict
set_custom_emoji_sticker_set_thumbnail_request_dict = set_custom_emoji_sticker_set_thumbnail_request_instance.to_dict()
# create an instance of SetCustomEmojiStickerSetThumbnailRequest from a dict
set_custom_emoji_sticker_set_thumbnail_request_from_dict = SetCustomEmojiStickerSetThumbnailRequest.from_dict(set_custom_emoji_sticker_set_thumbnail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


