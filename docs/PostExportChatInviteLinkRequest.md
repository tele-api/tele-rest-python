# PostExportChatInviteLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.post_export_chat_invite_link_request import PostExportChatInviteLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostExportChatInviteLinkRequest from a JSON string
post_export_chat_invite_link_request_instance = PostExportChatInviteLinkRequest.from_json(json)
# print the JSON string representation of the object
print(PostExportChatInviteLinkRequest.to_json())

# convert the object into a dict
post_export_chat_invite_link_request_dict = post_export_chat_invite_link_request_instance.to_dict()
# create an instance of PostExportChatInviteLinkRequest from a dict
post_export_chat_invite_link_request_from_dict = PostExportChatInviteLinkRequest.from_dict(post_export_chat_invite_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


