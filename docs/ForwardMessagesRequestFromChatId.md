# ForwardMessagesRequestFromChatId

Unique identifier for the chat where the original messages were sent (or channel username in the format `@channelusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.forward_messages_request_from_chat_id import ForwardMessagesRequestFromChatId

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardMessagesRequestFromChatId from a JSON string
forward_messages_request_from_chat_id_instance = ForwardMessagesRequestFromChatId.from_json(json)
# print the JSON string representation of the object
print(ForwardMessagesRequestFromChatId.to_json())

# convert the object into a dict
forward_messages_request_from_chat_id_dict = forward_messages_request_from_chat_id_instance.to_dict()
# create an instance of ForwardMessagesRequestFromChatId from a dict
forward_messages_request_from_chat_id_from_dict = ForwardMessagesRequestFromChatId.from_dict(forward_messages_request_from_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


