# PostForwardMessagesRequestFromChatId

Unique identifier for the chat where the original messages were sent (or channel username in the format `@channelusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_forward_messages_request_from_chat_id import PostForwardMessagesRequestFromChatId

# TODO update the JSON string below
json = "{}"
# create an instance of PostForwardMessagesRequestFromChatId from a JSON string
post_forward_messages_request_from_chat_id_instance = PostForwardMessagesRequestFromChatId.from_json(json)
# print the JSON string representation of the object
print(PostForwardMessagesRequestFromChatId.to_json())

# convert the object into a dict
post_forward_messages_request_from_chat_id_dict = post_forward_messages_request_from_chat_id_instance.to_dict()
# create an instance of PostForwardMessagesRequestFromChatId from a dict
post_forward_messages_request_from_chat_id_from_dict = PostForwardMessagesRequestFromChatId.from_dict(post_forward_messages_request_from_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


