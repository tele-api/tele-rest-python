# PostGetChatMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostLeaveChatRequestChatId**](PostLeaveChatRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.post_get_chat_member_request import PostGetChatMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetChatMemberRequest from a JSON string
post_get_chat_member_request_instance = PostGetChatMemberRequest.from_json(json)
# print the JSON string representation of the object
print(PostGetChatMemberRequest.to_json())

# convert the object into a dict
post_get_chat_member_request_dict = post_get_chat_member_request_instance.to_dict()
# create an instance of PostGetChatMemberRequest from a dict
post_get_chat_member_request_from_dict = PostGetChatMemberRequest.from_dict(post_get_chat_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


