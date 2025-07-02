# PostEditChatInviteLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**invite_link** | **str** | The invite link to edit | 
**name** | **str** | Invite link name; 0-32 characters | [optional] 
**expire_date** | **int** | Point in time (Unix timestamp) when the link will expire | [optional] 
**member_limit** | **int** | The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999 | [optional] 
**creates_join_request** | **bool** | *True*, if users joining the chat via the link need to be approved by chat administrators. If *True*, *member\\_limit* can&#39;t be specified | [optional] 

## Example

```python
from tele_rest.models.post_edit_chat_invite_link_request import PostEditChatInviteLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostEditChatInviteLinkRequest from a JSON string
post_edit_chat_invite_link_request_instance = PostEditChatInviteLinkRequest.from_json(json)
# print the JSON string representation of the object
print(PostEditChatInviteLinkRequest.to_json())

# convert the object into a dict
post_edit_chat_invite_link_request_dict = post_edit_chat_invite_link_request_instance.to_dict()
# create an instance of PostEditChatInviteLinkRequest from a dict
post_edit_chat_invite_link_request_from_dict = PostEditChatInviteLinkRequest.from_dict(post_edit_chat_invite_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


