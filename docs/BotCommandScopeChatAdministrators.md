# BotCommandScopeChatAdministrators

Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering all administrators of a specific group or supergroup chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scope type, must be *chat\\_administrators* | [default to 'chat_administrators']
**chat_id** | [**RestrictChatMemberPostRequestChatId**](RestrictChatMemberPostRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.bot_command_scope_chat_administrators import BotCommandScopeChatAdministrators

# TODO update the JSON string below
json = "{}"
# create an instance of BotCommandScopeChatAdministrators from a JSON string
bot_command_scope_chat_administrators_instance = BotCommandScopeChatAdministrators.from_json(json)
# print the JSON string representation of the object
print(BotCommandScopeChatAdministrators.to_json())

# convert the object into a dict
bot_command_scope_chat_administrators_dict = bot_command_scope_chat_administrators_instance.to_dict()
# create an instance of BotCommandScopeChatAdministrators from a dict
bot_command_scope_chat_administrators_from_dict = BotCommandScopeChatAdministrators.from_dict(bot_command_scope_chat_administrators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


