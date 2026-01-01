# ReplyParametersChatId

*Optional*. If the message to be replied to is from a different chat, unique identifier for the chat or username of the channel (in the format `@channelusername`). Not supported for messages sent on behalf of a business account and messages from channel direct messages chats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.reply_parameters_chat_id import ReplyParametersChatId

# TODO update the JSON string below
json = "{}"
# create an instance of ReplyParametersChatId from a JSON string
reply_parameters_chat_id_instance = ReplyParametersChatId.from_json(json)
# print the JSON string representation of the object
print(ReplyParametersChatId.to_json())

# convert the object into a dict
reply_parameters_chat_id_dict = reply_parameters_chat_id_instance.to_dict()
# create an instance of ReplyParametersChatId from a dict
reply_parameters_chat_id_from_dict = ReplyParametersChatId.from_dict(reply_parameters_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


