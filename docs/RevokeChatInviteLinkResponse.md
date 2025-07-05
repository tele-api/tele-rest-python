# RevokeChatInviteLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**ChatInviteLink**](ChatInviteLink.md) |  | 

## Example

```python
from tele_rest.models.revoke_chat_invite_link_response import RevokeChatInviteLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeChatInviteLinkResponse from a JSON string
revoke_chat_invite_link_response_instance = RevokeChatInviteLinkResponse.from_json(json)
# print the JSON string representation of the object
print(RevokeChatInviteLinkResponse.to_json())

# convert the object into a dict
revoke_chat_invite_link_response_dict = revoke_chat_invite_link_response_instance.to_dict()
# create an instance of RevokeChatInviteLinkResponse from a dict
revoke_chat_invite_link_response_from_dict = RevokeChatInviteLinkResponse.from_dict(revoke_chat_invite_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


