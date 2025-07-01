# BotCommandScope

This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:  * [BotCommandScopeDefault](https://core.telegram.org/bots/api/#botcommandscopedefault) * [BotCommandScopeAllPrivateChats](https://core.telegram.org/bots/api/#botcommandscopeallprivatechats) * [BotCommandScopeAllGroupChats](https://core.telegram.org/bots/api/#botcommandscopeallgroupchats) * [BotCommandScopeAllChatAdministrators](https://core.telegram.org/bots/api/#botcommandscopeallchatadministrators) * [BotCommandScopeChat](https://core.telegram.org/bots/api/#botcommandscopechat) * [BotCommandScopeChatAdministrators](https://core.telegram.org/bots/api/#botcommandscopechatadministrators) * [BotCommandScopeChatMember](https://core.telegram.org/bots/api/#botcommandscopechatmember)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scope type, must be *chat\\_member* | [default to 'chat_member']
**chat_id** | [**RestrictChatMemberPostRequestChatId**](RestrictChatMemberPostRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.bot_command_scope import BotCommandScope

# TODO update the JSON string below
json = "{}"
# create an instance of BotCommandScope from a JSON string
bot_command_scope_instance = BotCommandScope.from_json(json)
# print the JSON string representation of the object
print(BotCommandScope.to_json())

# convert the object into a dict
bot_command_scope_dict = bot_command_scope_instance.to_dict()
# create an instance of BotCommandScope from a dict
bot_command_scope_from_dict = BotCommandScope.from_dict(bot_command_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


