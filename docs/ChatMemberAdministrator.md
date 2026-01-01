# ChatMemberAdministrator

Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that has some additional privileges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The member&#39;s status in the chat, always “administrator” | [default to 'administrator']
**user** | [**User**](User.md) |  | 
**can_be_edited** | **bool** | *True*, if the bot is allowed to edit administrator privileges of that user | 
**is_anonymous** | **bool** | *True*, if the user&#39;s presence in the chat is hidden | 
**can_manage_chat** | **bool** | *True*, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages, ignore slow mode, and send messages to the chat without paying Telegram Stars. Implied by any other administrator privilege. | 
**can_delete_messages** | **bool** | *True*, if the administrator can delete messages of other users | 
**can_manage_video_chats** | **bool** | *True*, if the administrator can manage video chats | 
**can_restrict_members** | **bool** | *True*, if the administrator can restrict, ban or unban chat members, or access supergroup statistics | 
**can_promote_members** | **bool** | *True*, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user) | 
**can_change_info** | **bool** | *True*, if the user is allowed to change the chat title, photo and other settings | 
**can_invite_users** | **bool** | *True*, if the user is allowed to invite new users to the chat | 
**can_post_stories** | **bool** | *True*, if the administrator can post stories to the chat | 
**can_edit_stories** | **bool** | *True*, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat&#39;s story archive | 
**can_delete_stories** | **bool** | *True*, if the administrator can delete stories posted by other users | 
**can_post_messages** | **bool** | *Optional*. *True*, if the administrator can post messages in the channel, approve suggested posts, or access channel statistics; for channels only | [optional] 
**can_edit_messages** | **bool** | *Optional*. *True*, if the administrator can edit messages of other users and can pin messages; for channels only | [optional] 
**can_pin_messages** | **bool** | *Optional*. *True*, if the user is allowed to pin messages; for groups and supergroups only | [optional] 
**can_manage_topics** | **bool** | *Optional*. *True*, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only | [optional] 
**can_manage_direct_messages** | **bool** | *Optional*. *True*, if the administrator can manage direct messages of the channel and decline suggested posts; for channels only | [optional] 
**custom_title** | **str** | *Optional*. Custom title for this user | [optional] 

## Example

```python
from tele_rest.models.chat_member_administrator import ChatMemberAdministrator

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMemberAdministrator from a JSON string
chat_member_administrator_instance = ChatMemberAdministrator.from_json(json)
# print the JSON string representation of the object
print(ChatMemberAdministrator.to_json())

# convert the object into a dict
chat_member_administrator_dict = chat_member_administrator_instance.to_dict()
# create an instance of ChatMemberAdministrator from a dict
chat_member_administrator_from_dict = ChatMemberAdministrator.from_dict(chat_member_administrator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


