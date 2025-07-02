# ExportChatInviteLinkRequest

Request parameters for exportChatInviteLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.export_chat_invite_link_request import ExportChatInviteLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportChatInviteLinkRequest from a JSON string
export_chat_invite_link_request_instance = ExportChatInviteLinkRequest.from_json(json)
# print the JSON string representation of the object
print(ExportChatInviteLinkRequest.to_json())

# convert the object into a dict
export_chat_invite_link_request_dict = export_chat_invite_link_request_instance.to_dict()
# create an instance of ExportChatInviteLinkRequest from a dict
export_chat_invite_link_request_from_dict = ExportChatInviteLinkRequest.from_dict(export_chat_invite_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


