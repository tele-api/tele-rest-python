# ExportChatInviteLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **str** |  | 

## Example

```python
from tele_rest.models.export_chat_invite_link_response import ExportChatInviteLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportChatInviteLinkResponse from a JSON string
export_chat_invite_link_response_instance = ExportChatInviteLinkResponse.from_json(json)
# print the JSON string representation of the object
print(ExportChatInviteLinkResponse.to_json())

# convert the object into a dict
export_chat_invite_link_response_dict = export_chat_invite_link_response_instance.to_dict()
# create an instance of ExportChatInviteLinkResponse from a dict
export_chat_invite_link_response_from_dict = ExportChatInviteLinkResponse.from_dict(export_chat_invite_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


