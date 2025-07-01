# EditChatSubscriptionInviteLinkPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**invite_link** | **str** | The invite link to edit | 
**name** | **str** | Invite link name; 0-32 characters | [optional] 

## Example

```python
from tele_rest.models.edit_chat_subscription_invite_link_post_request import EditChatSubscriptionInviteLinkPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditChatSubscriptionInviteLinkPostRequest from a JSON string
edit_chat_subscription_invite_link_post_request_instance = EditChatSubscriptionInviteLinkPostRequest.from_json(json)
# print the JSON string representation of the object
print(EditChatSubscriptionInviteLinkPostRequest.to_json())

# convert the object into a dict
edit_chat_subscription_invite_link_post_request_dict = edit_chat_subscription_invite_link_post_request_instance.to_dict()
# create an instance of EditChatSubscriptionInviteLinkPostRequest from a dict
edit_chat_subscription_invite_link_post_request_from_dict = EditChatSubscriptionInviteLinkPostRequest.from_dict(edit_chat_subscription_invite_link_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


