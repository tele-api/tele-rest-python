# PostLeaveChatRequestChatId

Unique identifier for the target chat or username of the target supergroup or channel (in the format `@channelusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_leave_chat_request_chat_id import PostLeaveChatRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of PostLeaveChatRequestChatId from a JSON string
post_leave_chat_request_chat_id_instance = PostLeaveChatRequestChatId.from_json(json)
# print the JSON string representation of the object
print(PostLeaveChatRequestChatId.to_json())

# convert the object into a dict
post_leave_chat_request_chat_id_dict = post_leave_chat_request_chat_id_instance.to_dict()
# create an instance of PostLeaveChatRequestChatId from a dict
post_leave_chat_request_chat_id_from_dict = PostLeaveChatRequestChatId.from_dict(post_leave_chat_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


