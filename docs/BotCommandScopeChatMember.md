# BotCommandScopeChatMember

Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering a specific member of a group or supergroup chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scope type, must be *chat\\_member* | [default to 'chat_member']
**chat_id** | [**RestrictChatMemberPostRequestChatId**](RestrictChatMemberPostRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.bot_command_scope_chat_member import BotCommandScopeChatMember

# TODO update the JSON string below
json = "{}"
# create an instance of BotCommandScopeChatMember from a JSON string
bot_command_scope_chat_member_instance = BotCommandScopeChatMember.from_json(json)
# print the JSON string representation of the object
print(BotCommandScopeChatMember.to_json())

# convert the object into a dict
bot_command_scope_chat_member_dict = bot_command_scope_chat_member_instance.to_dict()
# create an instance of BotCommandScopeChatMember from a dict
bot_command_scope_chat_member_from_dict = BotCommandScopeChatMember.from_dict(bot_command_scope_chat_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


