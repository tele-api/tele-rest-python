# VideoChatScheduled

This object represents a service message about a video chat scheduled in the chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **int** | Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator | 

## Example

```python
from tele_rest.models.video_chat_scheduled import VideoChatScheduled

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChatScheduled from a JSON string
video_chat_scheduled_instance = VideoChatScheduled.from_json(json)
# print the JSON string representation of the object
print(VideoChatScheduled.to_json())

# convert the object into a dict
video_chat_scheduled_dict = video_chat_scheduled_instance.to_dict()
# create an instance of VideoChatScheduled from a dict
video_chat_scheduled_from_dict = VideoChatScheduled.from_dict(video_chat_scheduled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


