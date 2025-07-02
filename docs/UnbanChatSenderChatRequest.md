# UnbanChatSenderChatRequest

Request parameters for unbanChatSenderChat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**sender_chat_id** | **int** | Unique identifier of the target sender chat | 

## Example

```python
from tele_rest.models.unban_chat_sender_chat_request import UnbanChatSenderChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnbanChatSenderChatRequest from a JSON string
unban_chat_sender_chat_request_instance = UnbanChatSenderChatRequest.from_json(json)
# print the JSON string representation of the object
print(UnbanChatSenderChatRequest.to_json())

# convert the object into a dict
unban_chat_sender_chat_request_dict = unban_chat_sender_chat_request_instance.to_dict()
# create an instance of UnbanChatSenderChatRequest from a dict
unban_chat_sender_chat_request_from_dict = UnbanChatSenderChatRequest.from_dict(unban_chat_sender_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


