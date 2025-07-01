# BackgroundType

This object describes the type of a background. Currently, it can be one of  * [BackgroundTypeFill](https://core.telegram.org/bots/api/#backgroundtypefill) * [BackgroundTypeWallpaper](https://core.telegram.org/bots/api/#backgroundtypewallpaper) * [BackgroundTypePattern](https://core.telegram.org/bots/api/#backgroundtypepattern) * [BackgroundTypeChatTheme](https://core.telegram.org/bots/api/#backgroundtypechattheme)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the background, always “chat\\_theme” | [default to 'chat_theme']
**fill** | [**BackgroundFill**](BackgroundFill.md) |  | 
**dark_theme_dimming** | **int** | Dimming of the background in dark themes, as a percentage; 0-100 | 
**document** | [**Document**](Document.md) |  | 
**is_blurred** | **bool** | *Optional*. *True*, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12 | [optional] [default to True]
**is_moving** | **bool** | *Optional*. *True*, if the background moves slightly when the device is tilted | [optional] [default to True]
**intensity** | **int** | Intensity of the pattern when it is shown above the filled background; 0-100 | 
**is_inverted** | **bool** | *Optional*. *True*, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only | [optional] [default to True]
**theme_name** | **str** | Name of the chat theme, which is usually an emoji | 

## Example

```python
from tele_rest.models.background_type import BackgroundType

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundType from a JSON string
background_type_instance = BackgroundType.from_json(json)
# print the JSON string representation of the object
print(BackgroundType.to_json())

# convert the object into a dict
background_type_dict = background_type_instance.to_dict()
# create an instance of BackgroundType from a dict
background_type_from_dict = BackgroundType.from_dict(background_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


