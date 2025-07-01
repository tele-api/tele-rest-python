# ApproveChatJoinRequestPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.approve_chat_join_request_post_request import ApproveChatJoinRequestPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveChatJoinRequestPostRequest from a JSON string
approve_chat_join_request_post_request_instance = ApproveChatJoinRequestPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApproveChatJoinRequestPostRequest.to_json())

# convert the object into a dict
approve_chat_join_request_post_request_dict = approve_chat_join_request_post_request_instance.to_dict()
# create an instance of ApproveChatJoinRequestPostRequest from a dict
approve_chat_join_request_post_request_from_dict = ApproveChatJoinRequestPostRequest.from_dict(approve_chat_join_request_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


