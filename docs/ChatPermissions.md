# ChatPermissions

Describes actions that a non-administrator user is allowed to take in a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_send_messages** | **bool** | *Optional*. *True*, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues | [optional] 
**can_send_audios** | **bool** | *Optional*. *True*, if the user is allowed to send audios | [optional] 
**can_send_documents** | **bool** | *Optional*. *True*, if the user is allowed to send documents | [optional] 
**can_send_photos** | **bool** | *Optional*. *True*, if the user is allowed to send photos | [optional] 
**can_send_videos** | **bool** | *Optional*. *True*, if the user is allowed to send videos | [optional] 
**can_send_video_notes** | **bool** | *Optional*. *True*, if the user is allowed to send video notes | [optional] 
**can_send_voice_notes** | **bool** | *Optional*. *True*, if the user is allowed to send voice notes | [optional] 
**can_send_polls** | **bool** | *Optional*. *True*, if the user is allowed to send polls | [optional] 
**can_send_other_messages** | **bool** | *Optional*. *True*, if the user is allowed to send animations, games, stickers and use inline bots | [optional] 
**can_add_web_page_previews** | **bool** | *Optional*. *True*, if the user is allowed to add web page previews to their messages | [optional] 
**can_change_info** | **bool** | *Optional*. *True*, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups | [optional] 
**can_invite_users** | **bool** | *Optional*. *True*, if the user is allowed to invite new users to the chat | [optional] 
**can_pin_messages** | **bool** | *Optional*. *True*, if the user is allowed to pin messages. Ignored in public supergroups | [optional] 
**can_manage_topics** | **bool** | *Optional*. *True*, if the user is allowed to create forum topics. If omitted defaults to the value of can\\_pin\\_messages | [optional] 

## Example

```python
from tele_rest.models.chat_permissions import ChatPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of ChatPermissions from a JSON string
chat_permissions_instance = ChatPermissions.from_json(json)
# print the JSON string representation of the object
print(ChatPermissions.to_json())

# convert the object into a dict
chat_permissions_dict = chat_permissions_instance.to_dict()
# create an instance of ChatPermissions from a dict
chat_permissions_from_dict = ChatPermissions.from_dict(chat_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


