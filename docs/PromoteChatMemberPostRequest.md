# PromoteChatMemberPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 
**is_anonymous** | **bool** | Pass *True* if the administrator&#39;s presence in the chat is hidden | [optional] 
**can_manage_chat** | **bool** | Pass *True* if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege. | [optional] 
**can_delete_messages** | **bool** | Pass *True* if the administrator can delete messages of other users | [optional] 
**can_manage_video_chats** | **bool** | Pass *True* if the administrator can manage video chats | [optional] 
**can_restrict_members** | **bool** | Pass *True* if the administrator can restrict, ban or unban chat members, or access supergroup statistics | [optional] 
**can_promote_members** | **bool** | Pass *True* if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by him) | [optional] 
**can_change_info** | **bool** | Pass *True* if the administrator can change chat title, photo and other settings | [optional] 
**can_invite_users** | **bool** | Pass *True* if the administrator can invite new users to the chat | [optional] 
**can_post_stories** | **bool** | Pass *True* if the administrator can post stories to the chat | [optional] 
**can_edit_stories** | **bool** | Pass *True* if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat&#39;s story archive | [optional] 
**can_delete_stories** | **bool** | Pass *True* if the administrator can delete stories posted by other users | [optional] 
**can_post_messages** | **bool** | Pass *True* if the administrator can post messages in the channel, or access channel statistics; for channels only | [optional] 
**can_edit_messages** | **bool** | Pass *True* if the administrator can edit messages of other users and can pin messages; for channels only | [optional] 
**can_pin_messages** | **bool** | Pass *True* if the administrator can pin messages; for supergroups only | [optional] 
**can_manage_topics** | **bool** | Pass *True* if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only | [optional] 

## Example

```python
from tele_rest.models.promote_chat_member_post_request import PromoteChatMemberPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromoteChatMemberPostRequest from a JSON string
promote_chat_member_post_request_instance = PromoteChatMemberPostRequest.from_json(json)
# print the JSON string representation of the object
print(PromoteChatMemberPostRequest.to_json())

# convert the object into a dict
promote_chat_member_post_request_dict = promote_chat_member_post_request_instance.to_dict()
# create an instance of PromoteChatMemberPostRequest from a dict
promote_chat_member_post_request_from_dict = PromoteChatMemberPostRequest.from_dict(promote_chat_member_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


