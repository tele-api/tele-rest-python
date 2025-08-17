# VerifyChatRequestChatId

Unique identifier for the target chat or username of the target channel (in the format `@channelusername`). Channel direct messages chats can't be verified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.verify_chat_request_chat_id import VerifyChatRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyChatRequestChatId from a JSON string
verify_chat_request_chat_id_instance = VerifyChatRequestChatId.from_json(json)
# print the JSON string representation of the object
print(VerifyChatRequestChatId.to_json())

# convert the object into a dict
verify_chat_request_chat_id_dict = verify_chat_request_chat_id_instance.to_dict()
# create an instance of VerifyChatRequestChatId from a dict
verify_chat_request_chat_id_from_dict = VerifyChatRequestChatId.from_dict(verify_chat_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


