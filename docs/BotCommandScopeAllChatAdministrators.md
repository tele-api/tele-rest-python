# BotCommandScopeAllChatAdministrators

Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering all group and supergroup chat administrators.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scope type, must be *all\\_chat\\_administrators* | [default to 'all_chat_administrators']

## Example

```python
from tele_rest.models.bot_command_scope_all_chat_administrators import BotCommandScopeAllChatAdministrators

# TODO update the JSON string below
json = "{}"
# create an instance of BotCommandScopeAllChatAdministrators from a JSON string
bot_command_scope_all_chat_administrators_instance = BotCommandScopeAllChatAdministrators.from_json(json)
# print the JSON string representation of the object
print(BotCommandScopeAllChatAdministrators.to_json())

# convert the object into a dict
bot_command_scope_all_chat_administrators_dict = bot_command_scope_all_chat_administrators_instance.to_dict()
# create an instance of BotCommandScopeAllChatAdministrators from a dict
bot_command_scope_all_chat_administrators_from_dict = BotCommandScopeAllChatAdministrators.from_dict(bot_command_scope_all_chat_administrators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


