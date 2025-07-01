# BanChatSenderChatPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**sender_chat_id** | **int** | Unique identifier of the target sender chat | 

## Example

```python
from tele_rest.models.ban_chat_sender_chat_post_request import BanChatSenderChatPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BanChatSenderChatPostRequest from a JSON string
ban_chat_sender_chat_post_request_instance = BanChatSenderChatPostRequest.from_json(json)
# print the JSON string representation of the object
print(BanChatSenderChatPostRequest.to_json())

# convert the object into a dict
ban_chat_sender_chat_post_request_dict = ban_chat_sender_chat_post_request_instance.to_dict()
# create an instance of BanChatSenderChatPostRequest from a dict
ban_chat_sender_chat_post_request_from_dict = BanChatSenderChatPostRequest.from_dict(ban_chat_sender_chat_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


