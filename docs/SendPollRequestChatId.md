# SendPollRequestChatId

Unique identifier for the target chat or username of the target channel (in the format `@channelusername`). Polls can't be sent to channel direct messages chats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.send_poll_request_chat_id import SendPollRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of SendPollRequestChatId from a JSON string
send_poll_request_chat_id_instance = SendPollRequestChatId.from_json(json)
# print the JSON string representation of the object
print(SendPollRequestChatId.to_json())

# convert the object into a dict
send_poll_request_chat_id_dict = send_poll_request_chat_id_instance.to_dict()
# create an instance of SendPollRequestChatId from a dict
send_poll_request_chat_id_from_dict = SendPollRequestChatId.from_dict(send_poll_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


