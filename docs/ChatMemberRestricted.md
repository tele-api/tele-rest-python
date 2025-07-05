# ChatMemberRestricted

Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that is under certain restrictions in the chat. Supergroups only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The member&#39;s status in the chat, always “restricted” | [default to 'restricted']
**user** | [**User**](User.md) |  | 
**is_member** | **bool** | *True*, if the user is a member of the chat at the moment of the request | 
**can_send_messages** | **bool** | *True*, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues | 
**can_send_audios** | **bool** | *True*, if the user is allowed to send audios | 
**can_send_documents** | **bool** | *True*, if the user is allowed to send documents | 
**can_send_photos** | **bool** | *True*, if the user is allowed to send photos | 
**can_send_videos** | **bool** | *True*, if the user is allowed to send videos | 
**can_send_video_notes** | **bool** | *True*, if the user is allowed to send video notes | 
**can_send_voice_notes** | **bool** | *True*, if the user is allowed to send voice notes | 
**can_send_polls** | **bool** | *True*, if the user is allowed to send polls and checklists | 
**can_send_other_messages** | **bool** | *True*, if the user is allowed to send animations, games, stickers and use inline bots | 
**can_add_web_page_previews** | **bool** | *True*, if the user is allowed to add web page previews to their messages | 
**can_change_info** | **bool** | *True*, if the user is allowed to change the chat title, photo and other settings | 
**can_invite_users** | **bool** | *True*, if the user is allowed to invite new users to the chat | 
**can_pin_messages** | **bool** | *True*, if the user is allowed to pin messages | 
**can_manage_topics** | **bool** | *True*, if the user is allowed to create forum topics | 
**until_date** | **int** | Date when restrictions will be lifted for this user; Unix time. If 0, then the user is restricted forever | 

## Example

```python
from tele_rest.models.chat_member_restricted import ChatMemberRestricted

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMemberRestricted from a JSON string
chat_member_restricted_instance = ChatMemberRestricted.from_json(json)
# print the JSON string representation of the object
print(ChatMemberRestricted.to_json())

# convert the object into a dict
chat_member_restricted_dict = chat_member_restricted_instance.to_dict()
# create an instance of ChatMemberRestricted from a dict
chat_member_restricted_from_dict = ChatMemberRestricted.from_dict(chat_member_restricted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


