# RevokeChatInviteLinkPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RevokeChatInviteLinkPostRequestChatId**](RevokeChatInviteLinkPostRequestChatId.md) |  | 
**invite_link** | **str** | The invite link to revoke | 

## Example

```python
from tele_rest.models.revoke_chat_invite_link_post_request import RevokeChatInviteLinkPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeChatInviteLinkPostRequest from a JSON string
revoke_chat_invite_link_post_request_instance = RevokeChatInviteLinkPostRequest.from_json(json)
# print the JSON string representation of the object
print(RevokeChatInviteLinkPostRequest.to_json())

# convert the object into a dict
revoke_chat_invite_link_post_request_dict = revoke_chat_invite_link_post_request_instance.to_dict()
# create an instance of RevokeChatInviteLinkPostRequest from a dict
revoke_chat_invite_link_post_request_from_dict = RevokeChatInviteLinkPostRequest.from_dict(revoke_chat_invite_link_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


