# VideoChatEnded

This object represents a service message about a video chat ended in the chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | Video chat duration in seconds | 

## Example

```python
from tele_rest.models.video_chat_ended import VideoChatEnded

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChatEnded from a JSON string
video_chat_ended_instance = VideoChatEnded.from_json(json)
# print the JSON string representation of the object
print(VideoChatEnded.to_json())

# convert the object into a dict
video_chat_ended_dict = video_chat_ended_instance.to_dict()
# create an instance of VideoChatEnded from a dict
video_chat_ended_from_dict = VideoChatEnded.from_dict(video_chat_ended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


