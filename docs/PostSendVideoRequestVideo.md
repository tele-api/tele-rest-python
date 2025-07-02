# PostSendVideoRequestVideo

Video to send. Pass a file\\_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_send_video_request_video import PostSendVideoRequestVideo

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendVideoRequestVideo from a JSON string
post_send_video_request_video_instance = PostSendVideoRequestVideo.from_json(json)
# print the JSON string representation of the object
print(PostSendVideoRequestVideo.to_json())

# convert the object into a dict
post_send_video_request_video_dict = post_send_video_request_video_instance.to_dict()
# create an instance of PostSendVideoRequestVideo from a dict
post_send_video_request_video_from_dict = PostSendVideoRequestVideo.from_dict(post_send_video_request_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


