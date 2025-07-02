# PostRevokeChatInviteLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostRevokeChatInviteLinkRequestChatId**](PostRevokeChatInviteLinkRequestChatId.md) |  | 
**invite_link** | **str** | The invite link to revoke | 

## Example

```python
from tele_rest.models.post_revoke_chat_invite_link_request import PostRevokeChatInviteLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRevokeChatInviteLinkRequest from a JSON string
post_revoke_chat_invite_link_request_instance = PostRevokeChatInviteLinkRequest.from_json(json)
# print the JSON string representation of the object
print(PostRevokeChatInviteLinkRequest.to_json())

# convert the object into a dict
post_revoke_chat_invite_link_request_dict = post_revoke_chat_invite_link_request_instance.to_dict()
# create an instance of PostRevokeChatInviteLinkRequest from a dict
post_revoke_chat_invite_link_request_from_dict = PostRevokeChatInviteLinkRequest.from_dict(post_revoke_chat_invite_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


