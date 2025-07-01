# MenuButtonCommands

Represents a menu button, which opens the bot's list of commands.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the button, must be *commands* | [default to 'commands']

## Example

```python
from tele_rest.models.menu_button_commands import MenuButtonCommands

# TODO update the JSON string below
json = "{}"
# create an instance of MenuButtonCommands from a JSON string
menu_button_commands_instance = MenuButtonCommands.from_json(json)
# print the JSON string representation of the object
print(MenuButtonCommands.to_json())

# convert the object into a dict
menu_button_commands_dict = menu_button_commands_instance.to_dict()
# create an instance of MenuButtonCommands from a dict
menu_button_commands_from_dict = MenuButtonCommands.from_dict(menu_button_commands_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


