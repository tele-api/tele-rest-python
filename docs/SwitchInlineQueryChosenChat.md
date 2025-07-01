# SwitchInlineQueryChosenChat

This object represents an inline button that switches the current user to inline mode in a chosen chat, with an optional default inline query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | *Optional*. The default inline query to be inserted in the input field. If left empty, only the bot&#39;s username will be inserted | [optional] 
**allow_user_chats** | **bool** | *Optional*. True, if private chats with users can be chosen | [optional] 
**allow_bot_chats** | **bool** | *Optional*. True, if private chats with bots can be chosen | [optional] 
**allow_group_chats** | **bool** | *Optional*. True, if group and supergroup chats can be chosen | [optional] 
**allow_channel_chats** | **bool** | *Optional*. True, if channel chats can be chosen | [optional] 

## Example

```python
from tele_rest.models.switch_inline_query_chosen_chat import SwitchInlineQueryChosenChat

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchInlineQueryChosenChat from a JSON string
switch_inline_query_chosen_chat_instance = SwitchInlineQueryChosenChat.from_json(json)
# print the JSON string representation of the object
print(SwitchInlineQueryChosenChat.to_json())

# convert the object into a dict
switch_inline_query_chosen_chat_dict = switch_inline_query_chosen_chat_instance.to_dict()
# create an instance of SwitchInlineQueryChosenChat from a dict
switch_inline_query_chosen_chat_from_dict = SwitchInlineQueryChosenChat.from_dict(switch_inline_query_chosen_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


