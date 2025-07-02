# PostEditChatSubscriptionInviteLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**invite_link** | **str** | The invite link to edit | 
**name** | **str** | Invite link name; 0-32 characters | [optional] 

## Example

```python
from tele_rest.models.post_edit_chat_subscription_invite_link_request import PostEditChatSubscriptionInviteLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostEditChatSubscriptionInviteLinkRequest from a JSON string
post_edit_chat_subscription_invite_link_request_instance = PostEditChatSubscriptionInviteLinkRequest.from_json(json)
# print the JSON string representation of the object
print(PostEditChatSubscriptionInviteLinkRequest.to_json())

# convert the object into a dict
post_edit_chat_subscription_invite_link_request_dict = post_edit_chat_subscription_invite_link_request_instance.to_dict()
# create an instance of PostEditChatSubscriptionInviteLinkRequest from a dict
post_edit_chat_subscription_invite_link_request_from_dict = PostEditChatSubscriptionInviteLinkRequest.from_dict(post_edit_chat_subscription_invite_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


