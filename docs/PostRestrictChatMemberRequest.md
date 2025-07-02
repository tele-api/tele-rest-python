# PostRestrictChatMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostRestrictChatMemberRequestChatId**](PostRestrictChatMemberRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 
**permissions** | [**ChatPermissions**](ChatPermissions.md) |  | 
**use_independent_chat_permissions** | **bool** | Pass *True* if chat permissions are set independently. Otherwise, the *can\\_send\\_other\\_messages* and *can\\_add\\_web\\_page\\_previews* permissions will imply the *can\\_send\\_messages*, *can\\_send\\_audios*, *can\\_send\\_documents*, *can\\_send\\_photos*, *can\\_send\\_videos*, *can\\_send\\_video\\_notes*, and *can\\_send\\_voice\\_notes* permissions; the *can\\_send\\_polls* permission will imply the *can\\_send\\_messages* permission. | [optional] 
**until_date** | **int** | Date when restrictions will be lifted for the user; Unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever | [optional] 

## Example

```python
from tele_rest.models.post_restrict_chat_member_request import PostRestrictChatMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRestrictChatMemberRequest from a JSON string
post_restrict_chat_member_request_instance = PostRestrictChatMemberRequest.from_json(json)
# print the JSON string representation of the object
print(PostRestrictChatMemberRequest.to_json())

# convert the object into a dict
post_restrict_chat_member_request_dict = post_restrict_chat_member_request_instance.to_dict()
# create an instance of PostRestrictChatMemberRequest from a dict
post_restrict_chat_member_request_from_dict = PostRestrictChatMemberRequest.from_dict(post_restrict_chat_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


