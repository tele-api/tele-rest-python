# ExportChatInviteLinkPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.export_chat_invite_link_post_request import ExportChatInviteLinkPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportChatInviteLinkPostRequest from a JSON string
export_chat_invite_link_post_request_instance = ExportChatInviteLinkPostRequest.from_json(json)
# print the JSON string representation of the object
print(ExportChatInviteLinkPostRequest.to_json())

# convert the object into a dict
export_chat_invite_link_post_request_dict = export_chat_invite_link_post_request_instance.to_dict()
# create an instance of ExportChatInviteLinkPostRequest from a dict
export_chat_invite_link_post_request_from_dict = ExportChatInviteLinkPostRequest.from_dict(export_chat_invite_link_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


