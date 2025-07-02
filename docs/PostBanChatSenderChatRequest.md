# PostBanChatSenderChatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**sender_chat_id** | **int** | Unique identifier of the target sender chat | 

## Example

```python
from tele_rest.models.post_ban_chat_sender_chat_request import PostBanChatSenderChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostBanChatSenderChatRequest from a JSON string
post_ban_chat_sender_chat_request_instance = PostBanChatSenderChatRequest.from_json(json)
# print the JSON string representation of the object
print(PostBanChatSenderChatRequest.to_json())

# convert the object into a dict
post_ban_chat_sender_chat_request_dict = post_ban_chat_sender_chat_request_instance.to_dict()
# create an instance of PostBanChatSenderChatRequest from a dict
post_ban_chat_sender_chat_request_from_dict = PostBanChatSenderChatRequest.from_dict(post_ban_chat_sender_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


