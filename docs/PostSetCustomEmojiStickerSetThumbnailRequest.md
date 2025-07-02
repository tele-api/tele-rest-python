# PostSetCustomEmojiStickerSetThumbnailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sticker set name | 
**custom_emoji_id** | **str** | Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail. | [optional] 

## Example

```python
from tele_rest.models.post_set_custom_emoji_sticker_set_thumbnail_request import PostSetCustomEmojiStickerSetThumbnailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetCustomEmojiStickerSetThumbnailRequest from a JSON string
post_set_custom_emoji_sticker_set_thumbnail_request_instance = PostSetCustomEmojiStickerSetThumbnailRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetCustomEmojiStickerSetThumbnailRequest.to_json())

# convert the object into a dict
post_set_custom_emoji_sticker_set_thumbnail_request_dict = post_set_custom_emoji_sticker_set_thumbnail_request_instance.to_dict()
# create an instance of PostSetCustomEmojiStickerSetThumbnailRequest from a dict
post_set_custom_emoji_sticker_set_thumbnail_request_from_dict = PostSetCustomEmojiStickerSetThumbnailRequest.from_dict(post_set_custom_emoji_sticker_set_thumbnail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


