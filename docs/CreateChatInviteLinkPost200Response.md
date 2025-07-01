# CreateChatInviteLinkPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**ChatInviteLink**](ChatInviteLink.md) |  | 

## Example

```python
from tele_rest.models.create_chat_invite_link_post200_response import CreateChatInviteLinkPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatInviteLinkPost200Response from a JSON string
create_chat_invite_link_post200_response_instance = CreateChatInviteLinkPost200Response.from_json(json)
# print the JSON string representation of the object
print(CreateChatInviteLinkPost200Response.to_json())

# convert the object into a dict
create_chat_invite_link_post200_response_dict = create_chat_invite_link_post200_response_instance.to_dict()
# create an instance of CreateChatInviteLinkPost200Response from a dict
create_chat_invite_link_post200_response_from_dict = CreateChatInviteLinkPost200Response.from_dict(create_chat_invite_link_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


