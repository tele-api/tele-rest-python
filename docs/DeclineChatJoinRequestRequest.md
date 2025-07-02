# DeclineChatJoinRequestRequest

Request parameters for declineChatJoinRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.decline_chat_join_request_request import DeclineChatJoinRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeclineChatJoinRequestRequest from a JSON string
decline_chat_join_request_request_instance = DeclineChatJoinRequestRequest.from_json(json)
# print the JSON string representation of the object
print(DeclineChatJoinRequestRequest.to_json())

# convert the object into a dict
decline_chat_join_request_request_dict = decline_chat_join_request_request_instance.to_dict()
# create an instance of DeclineChatJoinRequestRequest from a dict
decline_chat_join_request_request_from_dict = DeclineChatJoinRequestRequest.from_dict(decline_chat_join_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


