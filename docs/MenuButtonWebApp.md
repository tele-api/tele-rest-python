# MenuButtonWebApp

Represents a menu button, which launches a [Web App](https://core.telegram.org/bots/webapps).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the button, must be *web\\_app* | [default to 'web_app']
**text** | **str** | Text on the button | 
**web_app** | [**WebAppInfo**](WebAppInfo.md) |  | 

## Example

```python
from tele_rest.models.menu_button_web_app import MenuButtonWebApp

# TODO update the JSON string below
json = "{}"
# create an instance of MenuButtonWebApp from a JSON string
menu_button_web_app_instance = MenuButtonWebApp.from_json(json)
# print the JSON string representation of the object
print(MenuButtonWebApp.to_json())

# convert the object into a dict
menu_button_web_app_dict = menu_button_web_app_instance.to_dict()
# create an instance of MenuButtonWebApp from a dict
menu_button_web_app_from_dict = MenuButtonWebApp.from_dict(menu_button_web_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


