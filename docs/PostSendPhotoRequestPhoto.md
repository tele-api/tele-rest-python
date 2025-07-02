# PostSendPhotoRequestPhoto

Photo to send. Pass a file\\_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_send_photo_request_photo import PostSendPhotoRequestPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendPhotoRequestPhoto from a JSON string
post_send_photo_request_photo_instance = PostSendPhotoRequestPhoto.from_json(json)
# print the JSON string representation of the object
print(PostSendPhotoRequestPhoto.to_json())

# convert the object into a dict
post_send_photo_request_photo_dict = post_send_photo_request_photo_instance.to_dict()
# create an instance of PostSendPhotoRequestPhoto from a dict
post_send_photo_request_photo_from_dict = PostSendPhotoRequestPhoto.from_dict(post_send_photo_request_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


