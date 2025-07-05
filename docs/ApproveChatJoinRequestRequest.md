# ApproveChatJoinRequestRequest

Request parameters for approveChatJoinRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.approve_chat_join_request_request import ApproveChatJoinRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveChatJoinRequestRequest from a JSON string
approve_chat_join_request_request_instance = ApproveChatJoinRequestRequest.from_json(json)
# print the JSON string representation of the object
print(ApproveChatJoinRequestRequest.to_json())

# convert the object into a dict
approve_chat_join_request_request_dict = approve_chat_join_request_request_instance.to_dict()
# create an instance of ApproveChatJoinRequestRequest from a dict
approve_chat_join_request_request_from_dict = ApproveChatJoinRequestRequest.from_dict(approve_chat_join_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


