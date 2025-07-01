# SendVideoPostRequestCover

Cover for the video in the message. Pass a file\\_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://\\<file\\_attach\\_name\\>” to upload a new one using multipart/form-data under \\<file\\_attach\\_name\\> name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.send_video_post_request_cover import SendVideoPostRequestCover

# TODO update the JSON string below
json = "{}"
# create an instance of SendVideoPostRequestCover from a JSON string
send_video_post_request_cover_instance = SendVideoPostRequestCover.from_json(json)
# print the JSON string representation of the object
print(SendVideoPostRequestCover.to_json())

# convert the object into a dict
send_video_post_request_cover_dict = send_video_post_request_cover_instance.to_dict()
# create an instance of SendVideoPostRequestCover from a dict
send_video_post_request_cover_from_dict = SendVideoPostRequestCover.from_dict(send_video_post_request_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


