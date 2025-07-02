# PostSendAudioRequestThumbnail

Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://\\<file\\_attach\\_name\\>” if the thumbnail was uploaded using multipart/form-data under \\<file\\_attach\\_name\\>. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_send_audio_request_thumbnail import PostSendAudioRequestThumbnail

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendAudioRequestThumbnail from a JSON string
post_send_audio_request_thumbnail_instance = PostSendAudioRequestThumbnail.from_json(json)
# print the JSON string representation of the object
print(PostSendAudioRequestThumbnail.to_json())

# convert the object into a dict
post_send_audio_request_thumbnail_dict = post_send_audio_request_thumbnail_instance.to_dict()
# create an instance of PostSendAudioRequestThumbnail from a dict
post_send_audio_request_thumbnail_from_dict = PostSendAudioRequestThumbnail.from_dict(post_send_audio_request_thumbnail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


