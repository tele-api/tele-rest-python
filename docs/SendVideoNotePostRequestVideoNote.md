# SendVideoNotePostRequestVideoNote

Video note to send. Pass a file\\_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files). Sending video notes by a URL is currently unsupported

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.send_video_note_post_request_video_note import SendVideoNotePostRequestVideoNote

# TODO update the JSON string below
json = "{}"
# create an instance of SendVideoNotePostRequestVideoNote from a JSON string
send_video_note_post_request_video_note_instance = SendVideoNotePostRequestVideoNote.from_json(json)
# print the JSON string representation of the object
print(SendVideoNotePostRequestVideoNote.to_json())

# convert the object into a dict
send_video_note_post_request_video_note_dict = send_video_note_post_request_video_note_instance.to_dict()
# create an instance of SendVideoNotePostRequestVideoNote from a dict
send_video_note_post_request_video_note_from_dict = SendVideoNotePostRequestVideoNote.from_dict(send_video_note_post_request_video_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


