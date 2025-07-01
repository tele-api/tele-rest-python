# BotCommandScopeDefault

Represents the default [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands. Default commands are used if no commands with a [narrower scope](https://core.telegram.org/bots/api/#determining-list-of-commands) are specified for the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scope type, must be *default* | [default to 'default']

## Example

```python
from tele_rest.models.bot_command_scope_default import BotCommandScopeDefault

# TODO update the JSON string below
json = "{}"
# create an instance of BotCommandScopeDefault from a JSON string
bot_command_scope_default_instance = BotCommandScopeDefault.from_json(json)
# print the JSON string representation of the object
print(BotCommandScopeDefault.to_json())

# convert the object into a dict
bot_command_scope_default_dict = bot_command_scope_default_instance.to_dict()
# create an instance of BotCommandScopeDefault from a dict
bot_command_scope_default_from_dict = BotCommandScopeDefault.from_dict(bot_command_scope_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


