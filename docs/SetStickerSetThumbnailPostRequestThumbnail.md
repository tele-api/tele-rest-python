# SetStickerSetThumbnailPostRequestThumbnail

A **.WEBP** or **.PNG** image with the thumbnail, must be up to 128 kilobytes in size and have a width and height of exactly 100px, or a **.TGS** animation with a thumbnail up to 32 kilobytes in size (see [https://core.telegram.org/stickers#animation-requirements](https://core.telegram.org/stickers#animation-requirements) for animated sticker technical requirements), or a **.WEBM** video with the thumbnail up to 32 kilobytes in size; see [https://core.telegram.org/stickers#video-requirements](https://core.telegram.org/stickers#video-requirements) for video sticker technical requirements. Pass a *file\\_id* as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files). Animated and video sticker set thumbnails can't be uploaded via HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.set_sticker_set_thumbnail_post_request_thumbnail import SetStickerSetThumbnailPostRequestThumbnail

# TODO update the JSON string below
json = "{}"
# create an instance of SetStickerSetThumbnailPostRequestThumbnail from a JSON string
set_sticker_set_thumbnail_post_request_thumbnail_instance = SetStickerSetThumbnailPostRequestThumbnail.from_json(json)
# print the JSON string representation of the object
print(SetStickerSetThumbnailPostRequestThumbnail.to_json())

# convert the object into a dict
set_sticker_set_thumbnail_post_request_thumbnail_dict = set_sticker_set_thumbnail_post_request_thumbnail_instance.to_dict()
# create an instance of SetStickerSetThumbnailPostRequestThumbnail from a dict
set_sticker_set_thumbnail_post_request_thumbnail_from_dict = SetStickerSetThumbnailPostRequestThumbnail.from_dict(set_sticker_set_thumbnail_post_request_thumbnail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


