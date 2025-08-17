# BotCommandScopeChatChatId

Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`). Channel direct messages chats and channel chats aren't supported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.bot_command_scope_chat_chat_id import BotCommandScopeChatChatId

# TODO update the JSON string below
json = "{}"
# create an instance of BotCommandScopeChatChatId from a JSON string
bot_command_scope_chat_chat_id_instance = BotCommandScopeChatChatId.from_json(json)
# print the JSON string representation of the object
print(BotCommandScopeChatChatId.to_json())

# convert the object into a dict
bot_command_scope_chat_chat_id_dict = bot_command_scope_chat_chat_id_instance.to_dict()
# create an instance of BotCommandScopeChatChatId from a dict
bot_command_scope_chat_chat_id_from_dict = BotCommandScopeChatChatId.from_dict(bot_command_scope_chat_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


