# LeaveChatRequestChatId

Unique identifier for the target chat or username of the target supergroup or channel (in the format `@channelusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.leave_chat_request_chat_id import LeaveChatRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveChatRequestChatId from a JSON string
leave_chat_request_chat_id_instance = LeaveChatRequestChatId.from_json(json)
# print the JSON string representation of the object
print(LeaveChatRequestChatId.to_json())

# convert the object into a dict
leave_chat_request_chat_id_dict = leave_chat_request_chat_id_instance.to_dict()
# create an instance of LeaveChatRequestChatId from a dict
leave_chat_request_chat_id_from_dict = LeaveChatRequestChatId.from_dict(leave_chat_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


