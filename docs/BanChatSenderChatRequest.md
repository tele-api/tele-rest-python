# BanChatSenderChatRequest

Request parameters for banChatSenderChat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**sender_chat_id** | **int** | Unique identifier of the target sender chat | 

## Example

```python
from tele_rest.models.ban_chat_sender_chat_request import BanChatSenderChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BanChatSenderChatRequest from a JSON string
ban_chat_sender_chat_request_instance = BanChatSenderChatRequest.from_json(json)
# print the JSON string representation of the object
print(BanChatSenderChatRequest.to_json())

# convert the object into a dict
ban_chat_sender_chat_request_dict = ban_chat_sender_chat_request_instance.to_dict()
# create an instance of BanChatSenderChatRequest from a dict
ban_chat_sender_chat_request_from_dict = BanChatSenderChatRequest.from_dict(ban_chat_sender_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


