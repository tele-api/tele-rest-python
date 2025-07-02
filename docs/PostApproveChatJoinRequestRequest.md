# PostApproveChatJoinRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.post_approve_chat_join_request_request import PostApproveChatJoinRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostApproveChatJoinRequestRequest from a JSON string
post_approve_chat_join_request_request_instance = PostApproveChatJoinRequestRequest.from_json(json)
# print the JSON string representation of the object
print(PostApproveChatJoinRequestRequest.to_json())

# convert the object into a dict
post_approve_chat_join_request_request_dict = post_approve_chat_join_request_request_instance.to_dict()
# create an instance of PostApproveChatJoinRequestRequest from a dict
post_approve_chat_join_request_request_from_dict = PostApproveChatJoinRequestRequest.from_dict(post_approve_chat_join_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


