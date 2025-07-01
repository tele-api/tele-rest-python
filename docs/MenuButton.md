# MenuButton

This object describes the bot's menu button in a private chat. It should be one of  * [MenuButtonCommands](https://core.telegram.org/bots/api/#menubuttoncommands) * [MenuButtonWebApp](https://core.telegram.org/bots/api/#menubuttonwebapp) * [MenuButtonDefault](https://core.telegram.org/bots/api/#menubuttondefault)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the button, must be *default* | [default to 'default']
**text** | **str** | Text on the button | 
**web_app** | [**WebAppInfo**](WebAppInfo.md) |  | 

## Example

```python
from tele_rest.models.menu_button import MenuButton

# TODO update the JSON string below
json = "{}"
# create an instance of MenuButton from a JSON string
menu_button_instance = MenuButton.from_json(json)
# print the JSON string representation of the object
print(MenuButton.to_json())

# convert the object into a dict
menu_button_dict = menu_button_instance.to_dict()
# create an instance of MenuButton from a dict
menu_button_from_dict = MenuButton.from_dict(menu_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


