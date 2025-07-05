# SendMessageRequestChatId

Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.send_message_request_chat_id import SendMessageRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessageRequestChatId from a JSON string
send_message_request_chat_id_instance = SendMessageRequestChatId.from_json(json)
# print the JSON string representation of the object
print(SendMessageRequestChatId.to_json())

# convert the object into a dict
send_message_request_chat_id_dict = send_message_request_chat_id_instance.to_dict()
# create an instance of SendMessageRequestChatId from a dict
send_message_request_chat_id_from_dict = SendMessageRequestChatId.from_dict(send_message_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


