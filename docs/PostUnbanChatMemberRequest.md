# PostUnbanChatMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostBanChatMemberRequestChatId**](PostBanChatMemberRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 
**only_if_banned** | **bool** | Do nothing if the user is not banned | [optional] 

## Example

```python
from tele_rest.models.post_unban_chat_member_request import PostUnbanChatMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostUnbanChatMemberRequest from a JSON string
post_unban_chat_member_request_instance = PostUnbanChatMemberRequest.from_json(json)
# print the JSON string representation of the object
print(PostUnbanChatMemberRequest.to_json())

# convert the object into a dict
post_unban_chat_member_request_dict = post_unban_chat_member_request_instance.to_dict()
# create an instance of PostUnbanChatMemberRequest from a dict
post_unban_chat_member_request_from_dict = PostUnbanChatMemberRequest.from_dict(post_unban_chat_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


