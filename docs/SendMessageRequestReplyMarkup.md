# SendMessageRequestReplyMarkup

Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline_keyboard** | **List[List[InlineKeyboardButton]]** | Array of button rows, each represented by an Array of [InlineKeyboardButton](https://core.telegram.org/bots/api/#inlinekeyboardbutton) objects | 
**keyboard** | **List[List[KeyboardButton]]** | Array of button rows, each represented by an Array of [KeyboardButton](https://core.telegram.org/bots/api/#keyboardbutton) objects | 
**is_persistent** | **bool** | *Optional*. Requests clients to always show the keyboard when the regular keyboard is hidden. Defaults to *false*, in which case the custom keyboard can be hidden and opened with a keyboard icon. | [optional] [default to False]
**resize_keyboard** | **bool** | *Optional*. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to *false*, in which case the custom keyboard is always of the same height as the app&#39;s standard keyboard. | [optional] [default to False]
**one_time_keyboard** | **bool** | *Optional*. Requests clients to hide the keyboard as soon as it&#39;s been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can press a special button in the input field to see the custom keyboard again. Defaults to *false*. | [optional] [default to False]
**input_field_placeholder** | **str** | *Optional*. The placeholder to be shown in the input field when the reply is active; 1-64 characters | [optional] 
**selective** | **bool** | *Optional*. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the *text* of the [Message](https://core.telegram.org/bots/api/#message) object; 2) if the bot&#39;s message is a reply to a message in the same chat and forum topic, sender of the original message. | [optional] 
**remove_keyboard** | **bool** | Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use *one\\_time\\_keyboard* in [ReplyKeyboardMarkup](https://core.telegram.org/bots/api/#replykeyboardmarkup)) | [default to True]
**force_reply** | **bool** | Shows reply interface to the user, as if they manually selected the bot&#39;s message and tapped &#39;Reply&#39; | [default to True]

## Example

```python
from tele_rest.models.send_message_request_reply_markup import SendMessageRequestReplyMarkup

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessageRequestReplyMarkup from a JSON string
send_message_request_reply_markup_instance = SendMessageRequestReplyMarkup.from_json(json)
# print the JSON string representation of the object
print(SendMessageRequestReplyMarkup.to_json())

# convert the object into a dict
send_message_request_reply_markup_dict = send_message_request_reply_markup_instance.to_dict()
# create an instance of SendMessageRequestReplyMarkup from a dict
send_message_request_reply_markup_from_dict = SendMessageRequestReplyMarkup.from_dict(send_message_request_reply_markup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


