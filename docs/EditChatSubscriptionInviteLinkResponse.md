# EditChatSubscriptionInviteLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**ChatInviteLink**](ChatInviteLink.md) |  | 

## Example

```python
from tele_rest.models.edit_chat_subscription_invite_link_response import EditChatSubscriptionInviteLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditChatSubscriptionInviteLinkResponse from a JSON string
edit_chat_subscription_invite_link_response_instance = EditChatSubscriptionInviteLinkResponse.from_json(json)
# print the JSON string representation of the object
print(EditChatSubscriptionInviteLinkResponse.to_json())

# convert the object into a dict
edit_chat_subscription_invite_link_response_dict = edit_chat_subscription_invite_link_response_instance.to_dict()
# create an instance of EditChatSubscriptionInviteLinkResponse from a dict
edit_chat_subscription_invite_link_response_from_dict = EditChatSubscriptionInviteLinkResponse.from_dict(edit_chat_subscription_invite_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


