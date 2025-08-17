# InlineKeyboardButton

This object represents one button of an inline keyboard. Exactly one of the optional fields must be used to specify type of the button.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Label text on the button | 
**url** | **str** | *Optional*. HTTP or tg:// URL to be opened when the button is pressed. Links &#x60;tg://user?id&#x3D;&lt;user_id&gt;&#x60; can be used to mention a user by their identifier without using a username, if this is allowed by their privacy settings. | [optional] 
**callback_data** | **str** | *Optional*. Data to be sent in a [callback query](https://core.telegram.org/bots/api/#callbackquery) to the bot when the button is pressed, 1-64 bytes | [optional] 
**web_app** | [**WebAppInfo**](WebAppInfo.md) |  | [optional] 
**login_url** | [**LoginUrl**](LoginUrl.md) |  | [optional] 
**switch_inline_query** | **str** | *Optional*. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot&#39;s username and the specified inline query in the input field. May be empty, in which case just the bot&#39;s username will be inserted. Not supported for messages sent in channel direct messages chats and on behalf of a Telegram Business account. | [optional] 
**switch_inline_query_current_chat** | **str** | *Optional*. If set, pressing the button will insert the bot&#39;s username and the specified inline query in the current chat&#39;s input field. May be empty, in which case only the bot&#39;s username will be inserted.    This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. Not supported in channels and for messages sent in channel direct messages chats and on behalf of a Telegram Business account. | [optional] 
**switch_inline_query_chosen_chat** | [**SwitchInlineQueryChosenChat**](SwitchInlineQueryChosenChat.md) |  | [optional] 
**copy_text** | [**CopyTextButton**](CopyTextButton.md) |  | [optional] 
**callback_game** | **object** |  | [optional] 
**pay** | **bool** | *Optional*. Specify *True*, to send a [Pay button](https://core.telegram.org/bots/api/#payments). Substrings “⭐” and “XTR” in the buttons&#39;s text will be replaced with a Telegram Star icon.    **NOTE:** This type of button **must** always be the first button in the first row and can only be used in invoice messages. | [optional] 

## Example

```python
from tele_rest.models.inline_keyboard_button import InlineKeyboardButton

# TODO update the JSON string below
json = "{}"
# create an instance of InlineKeyboardButton from a JSON string
inline_keyboard_button_instance = InlineKeyboardButton.from_json(json)
# print the JSON string representation of the object
print(InlineKeyboardButton.to_json())

# convert the object into a dict
inline_keyboard_button_dict = inline_keyboard_button_instance.to_dict()
# create an instance of InlineKeyboardButton from a dict
inline_keyboard_button_from_dict = InlineKeyboardButton.from_dict(inline_keyboard_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


