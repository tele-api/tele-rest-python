# BackgroundTypeWallpaper

The background is a wallpaper in the JPEG format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the background, always “wallpaper” | [default to 'wallpaper']
**document** | [**Document**](Document.md) |  | 
**dark_theme_dimming** | **int** | Dimming of the background in dark themes, as a percentage; 0-100 | 
**is_blurred** | **bool** | *Optional*. *True*, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12 | [optional] [default to True]
**is_moving** | **bool** | *Optional*. *True*, if the background moves slightly when the device is tilted | [optional] [default to True]

## Example

```python
from tele_rest.models.background_type_wallpaper import BackgroundTypeWallpaper

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundTypeWallpaper from a JSON string
background_type_wallpaper_instance = BackgroundTypeWallpaper.from_json(json)
# print the JSON string representation of the object
print(BackgroundTypeWallpaper.to_json())

# convert the object into a dict
background_type_wallpaper_dict = background_type_wallpaper_instance.to_dict()
# create an instance of BackgroundTypeWallpaper from a dict
background_type_wallpaper_from_dict = BackgroundTypeWallpaper.from_dict(background_type_wallpaper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


