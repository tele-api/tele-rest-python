# SendChatActionRequestChatId

Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`). Channel chats and channel direct messages chats aren't supported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.send_chat_action_request_chat_id import SendChatActionRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of SendChatActionRequestChatId from a JSON string
send_chat_action_request_chat_id_instance = SendChatActionRequestChatId.from_json(json)
# print the JSON string representation of the object
print(SendChatActionRequestChatId.to_json())

# convert the object into a dict
send_chat_action_request_chat_id_dict = send_chat_action_request_chat_id_instance.to_dict()
# create an instance of SendChatActionRequestChatId from a dict
send_chat_action_request_chat_id_from_dict = SendChatActionRequestChatId.from_dict(send_chat_action_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


