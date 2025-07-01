# MenuButtonDefault

Describes that no specific value for the menu button was set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the button, must be *default* | [default to 'default']

## Example

```python
from tele_rest.models.menu_button_default import MenuButtonDefault

# TODO update the JSON string below
json = "{}"
# create an instance of MenuButtonDefault from a JSON string
menu_button_default_instance = MenuButtonDefault.from_json(json)
# print the JSON string representation of the object
print(MenuButtonDefault.to_json())

# convert the object into a dict
menu_button_default_dict = menu_button_default_instance.to_dict()
# create an instance of MenuButtonDefault from a dict
menu_button_default_from_dict = MenuButtonDefault.from_dict(menu_button_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


