# SetChatPermissionsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberPostRequestChatId**](RestrictChatMemberPostRequestChatId.md) |  | 
**permissions** | [**ChatPermissions**](ChatPermissions.md) |  | 
**use_independent_chat_permissions** | **bool** | Pass *True* if chat permissions are set independently. Otherwise, the *can\\_send\\_other\\_messages* and *can\\_add\\_web\\_page\\_previews* permissions will imply the *can\\_send\\_messages*, *can\\_send\\_audios*, *can\\_send\\_documents*, *can\\_send\\_photos*, *can\\_send\\_videos*, *can\\_send\\_video\\_notes*, and *can\\_send\\_voice\\_notes* permissions; the *can\\_send\\_polls* permission will imply the *can\\_send\\_messages* permission. | [optional] 

## Example

```python
from tele_rest.models.set_chat_permissions_post_request import SetChatPermissionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatPermissionsPostRequest from a JSON string
set_chat_permissions_post_request_instance = SetChatPermissionsPostRequest.from_json(json)
# print the JSON string representation of the object
print(SetChatPermissionsPostRequest.to_json())

# convert the object into a dict
set_chat_permissions_post_request_dict = set_chat_permissions_post_request_instance.to_dict()
# create an instance of SetChatPermissionsPostRequest from a dict
set_chat_permissions_post_request_from_dict = SetChatPermissionsPostRequest.from_dict(set_chat_permissions_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


