# ChatInviteLink

Represents an invite link for a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invite_link** | **str** | The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with “…”. | 
**creator** | [**User**](User.md) |  | 
**creates_join_request** | **bool** | *True*, if users joining the chat via the link need to be approved by chat administrators | 
**is_primary** | **bool** | *True*, if the link is primary | 
**is_revoked** | **bool** | *True*, if the link is revoked | 
**name** | **str** | *Optional*. Invite link name | [optional] 
**expire_date** | **int** | *Optional*. Point in time (Unix timestamp) when the link will expire or has been expired | [optional] 
**member_limit** | **int** | *Optional*. The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999 | [optional] 
**pending_join_request_count** | **int** | *Optional*. Number of pending join requests created using this link | [optional] 
**subscription_period** | **int** | *Optional*. The number of seconds the subscription will be active for before the next payment | [optional] 
**subscription_price** | **int** | *Optional*. The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat using the link | [optional] 

## Example

```python
from tele_rest.models.chat_invite_link import ChatInviteLink

# TODO update the JSON string below
json = "{}"
# create an instance of ChatInviteLink from a JSON string
chat_invite_link_instance = ChatInviteLink.from_json(json)
# print the JSON string representation of the object
print(ChatInviteLink.to_json())

# convert the object into a dict
chat_invite_link_dict = chat_invite_link_instance.to_dict()
# create an instance of ChatInviteLink from a dict
chat_invite_link_from_dict = ChatInviteLink.from_dict(chat_invite_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


