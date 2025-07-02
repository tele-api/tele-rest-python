# BanChatSenderChatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.ban_chat_sender_chat_response import BanChatSenderChatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BanChatSenderChatResponse from a JSON string
ban_chat_sender_chat_response_instance = BanChatSenderChatResponse.from_json(json)
# print the JSON string representation of the object
print(BanChatSenderChatResponse.to_json())

# convert the object into a dict
ban_chat_sender_chat_response_dict = ban_chat_sender_chat_response_instance.to_dict()
# create an instance of BanChatSenderChatResponse from a dict
ban_chat_sender_chat_response_from_dict = BanChatSenderChatResponse.from_dict(ban_chat_sender_chat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


