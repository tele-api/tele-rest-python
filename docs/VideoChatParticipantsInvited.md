# VideoChatParticipantsInvited

This object represents a service message about new members invited to a video chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[User]**](User.md) | New members that were invited to the video chat | 

## Example

```python
from tele_rest.models.video_chat_participants_invited import VideoChatParticipantsInvited

# TODO update the JSON string below
json = "{}"
# create an instance of VideoChatParticipantsInvited from a JSON string
video_chat_participants_invited_instance = VideoChatParticipantsInvited.from_json(json)
# print the JSON string representation of the object
print(VideoChatParticipantsInvited.to_json())

# convert the object into a dict
video_chat_participants_invited_dict = video_chat_participants_invited_instance.to_dict()
# create an instance of VideoChatParticipantsInvited from a dict
video_chat_participants_invited_from_dict = VideoChatParticipantsInvited.from_dict(video_chat_participants_invited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


