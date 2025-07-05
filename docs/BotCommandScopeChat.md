# BotCommandScopeChat

Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering a specific chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scope type, must be *chat* | [default to 'chat']
**chat_id** | [**BotCommandScopeChatChatId**](BotCommandScopeChatChatId.md) |  | 

## Example

```python
from tele_rest.models.bot_command_scope_chat import BotCommandScopeChat

# TODO update the JSON string below
json = "{}"
# create an instance of BotCommandScopeChat from a JSON string
bot_command_scope_chat_instance = BotCommandScopeChat.from_json(json)
# print the JSON string representation of the object
print(BotCommandScopeChat.to_json())

# convert the object into a dict
bot_command_scope_chat_dict = bot_command_scope_chat_instance.to_dict()
# create an instance of BotCommandScopeChat from a dict
bot_command_scope_chat_from_dict = BotCommandScopeChat.from_dict(bot_command_scope_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


