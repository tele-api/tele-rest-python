# PostSendVideoRequestCover

Cover for the video in the message. Pass a file\\_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://\\<file\\_attach\\_name\\>” to upload a new one using multipart/form-data under \\<file\\_attach\\_name\\> name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_send_video_request_cover import PostSendVideoRequestCover

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendVideoRequestCover from a JSON string
post_send_video_request_cover_instance = PostSendVideoRequestCover.from_json(json)
# print the JSON string representation of the object
print(PostSendVideoRequestCover.to_json())

# convert the object into a dict
post_send_video_request_cover_dict = post_send_video_request_cover_instance.to_dict()
# create an instance of PostSendVideoRequestCover from a dict
post_send_video_request_cover_from_dict = PostSendVideoRequestCover.from_dict(post_send_video_request_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


