# BotCommandScopeAllGroupChats

Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering all group and supergroup chats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scope type, must be *all\\_group\\_chats* | [default to 'all_group_chats']

## Example

```python
from tele_rest.models.bot_command_scope_all_group_chats import BotCommandScopeAllGroupChats

# TODO update the JSON string below
json = "{}"
# create an instance of BotCommandScopeAllGroupChats from a JSON string
bot_command_scope_all_group_chats_instance = BotCommandScopeAllGroupChats.from_json(json)
# print the JSON string representation of the object
print(BotCommandScopeAllGroupChats.to_json())

# convert the object into a dict
bot_command_scope_all_group_chats_dict = bot_command_scope_all_group_chats_instance.to_dict()
# create an instance of BotCommandScopeAllGroupChats from a dict
bot_command_scope_all_group_chats_from_dict = BotCommandScopeAllGroupChats.from_dict(bot_command_scope_all_group_chats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


