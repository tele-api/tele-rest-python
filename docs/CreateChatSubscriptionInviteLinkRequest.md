# CreateChatSubscriptionInviteLinkRequest

Request parameters for createChatSubscriptionInviteLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**CreateChatSubscriptionInviteLinkRequestChatId**](CreateChatSubscriptionInviteLinkRequestChatId.md) |  | 
**name** | **str** | Invite link name; 0-32 characters | [optional] 
**subscription_period** | **int** | The number of seconds the subscription will be active for before the next payment. Currently, it must always be 2592000 (30 days). | 
**subscription_price** | **int** | The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat; 1-10000 | 

## Example

```python
from tele_rest.models.create_chat_subscription_invite_link_request import CreateChatSubscriptionInviteLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatSubscriptionInviteLinkRequest from a JSON string
create_chat_subscription_invite_link_request_instance = CreateChatSubscriptionInviteLinkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateChatSubscriptionInviteLinkRequest.to_json())

# convert the object into a dict
create_chat_subscription_invite_link_request_dict = create_chat_subscription_invite_link_request_instance.to_dict()
# create an instance of CreateChatSubscriptionInviteLinkRequest from a dict
create_chat_subscription_invite_link_request_from_dict = CreateChatSubscriptionInviteLinkRequest.from_dict(create_chat_subscription_invite_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


