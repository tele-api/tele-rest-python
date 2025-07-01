# ChatMemberUpdated

This object represents changes in the status of a chat member.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**Chat**](Chat.md) |  | 
**var_from** | [**User**](User.md) |  | 
**var_date** | **int** | Date the change was done in Unix time | 
**old_chat_member** | [**ChatMember**](ChatMember.md) |  | 
**new_chat_member** | [**ChatMember**](ChatMember.md) |  | 
**invite_link** | [**ChatInviteLink**](ChatInviteLink.md) |  | [optional] 
**via_join_request** | **bool** | *Optional*. True, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator | [optional] 
**via_chat_folder_invite_link** | **bool** | *Optional*. True, if the user joined the chat via a chat folder invite link | [optional] 

## Example

```python
from tele_rest.models.chat_member_updated import ChatMemberUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMemberUpdated from a JSON string
chat_member_updated_instance = ChatMemberUpdated.from_json(json)
# print the JSON string representation of the object
print(ChatMemberUpdated.to_json())

# convert the object into a dict
chat_member_updated_dict = chat_member_updated_instance.to_dict()
# create an instance of ChatMemberUpdated from a dict
chat_member_updated_from_dict = ChatMemberUpdated.from_dict(chat_member_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


