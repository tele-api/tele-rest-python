# BotCommandScopeAllPrivateChats

Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering all private chats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scope type, must be *all\\_private\\_chats* | [default to 'all_private_chats']

## Example

```python
from tele_rest.models.bot_command_scope_all_private_chats import BotCommandScopeAllPrivateChats

# TODO update the JSON string below
json = "{}"
# create an instance of BotCommandScopeAllPrivateChats from a JSON string
bot_command_scope_all_private_chats_instance = BotCommandScopeAllPrivateChats.from_json(json)
# print the JSON string representation of the object
print(BotCommandScopeAllPrivateChats.to_json())

# convert the object into a dict
bot_command_scope_all_private_chats_dict = bot_command_scope_all_private_chats_instance.to_dict()
# create an instance of BotCommandScopeAllPrivateChats from a dict
bot_command_scope_all_private_chats_from_dict = BotCommandScopeAllPrivateChats.from_dict(bot_command_scope_all_private_chats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


