# CreateChatInviteLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**ChatInviteLink**](ChatInviteLink.md) |  | 

## Example

```python
from tele_rest.models.create_chat_invite_link_response import CreateChatInviteLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatInviteLinkResponse from a JSON string
create_chat_invite_link_response_instance = CreateChatInviteLinkResponse.from_json(json)
# print the JSON string representation of the object
print(CreateChatInviteLinkResponse.to_json())

# convert the object into a dict
create_chat_invite_link_response_dict = create_chat_invite_link_response_instance.to_dict()
# create an instance of CreateChatInviteLinkResponse from a dict
create_chat_invite_link_response_from_dict = CreateChatInviteLinkResponse.from_dict(create_chat_invite_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


