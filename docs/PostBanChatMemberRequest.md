# PostBanChatMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostBanChatMemberRequestChatId**](PostBanChatMemberRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 
**until_date** | **int** | Date when the user will be unbanned; Unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only. | [optional] 
**revoke_messages** | **bool** | Pass *True* to delete all messages from the chat for the user that is being removed. If *False*, the user will be able to see messages in the group that were sent before the user was removed. Always *True* for supergroups and channels. | [optional] 

## Example

```python
from tele_rest.models.post_ban_chat_member_request import PostBanChatMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostBanChatMemberRequest from a JSON string
post_ban_chat_member_request_instance = PostBanChatMemberRequest.from_json(json)
# print the JSON string representation of the object
print(PostBanChatMemberRequest.to_json())

# convert the object into a dict
post_ban_chat_member_request_dict = post_ban_chat_member_request_instance.to_dict()
# create an instance of PostBanChatMemberRequest from a dict
post_ban_chat_member_request_from_dict = PostBanChatMemberRequest.from_dict(post_ban_chat_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


