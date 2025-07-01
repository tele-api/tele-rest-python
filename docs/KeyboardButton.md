# KeyboardButton

This object represents one button of the reply keyboard. At most one of the optional fields must be used to specify type of the button. For simple text buttons, *String* can be used instead of this object to specify the button text.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed | 
**request_users** | [**KeyboardButtonRequestUsers**](KeyboardButtonRequestUsers.md) |  | [optional] 
**request_chat** | [**KeyboardButtonRequestChat**](KeyboardButtonRequestChat.md) |  | [optional] 
**request_contact** | **bool** | *Optional*. If *True*, the user&#39;s phone number will be sent as a contact when the button is pressed. Available in private chats only. | [optional] 
**request_location** | **bool** | *Optional*. If *True*, the user&#39;s current location will be sent when the button is pressed. Available in private chats only. | [optional] 
**request_poll** | [**KeyboardButtonPollType**](KeyboardButtonPollType.md) |  | [optional] 
**web_app** | [**WebAppInfo**](WebAppInfo.md) |  | [optional] 

## Example

```python
from tele_rest.models.keyboard_button import KeyboardButton

# TODO update the JSON string below
json = "{}"
# create an instance of KeyboardButton from a JSON string
keyboard_button_instance = KeyboardButton.from_json(json)
# print the JSON string representation of the object
print(KeyboardButton.to_json())

# convert the object into a dict
keyboard_button_dict = keyboard_button_instance.to_dict()
# create an instance of KeyboardButton from a dict
keyboard_button_from_dict = KeyboardButton.from_dict(keyboard_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


