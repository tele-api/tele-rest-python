# StoryAreaTypeWeather

Describes a story area containing weather information. Currently, a story can have up to 3 weather areas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the area, always “weather” | [default to 'weather']
**temperature** | **float** | Temperature, in degree Celsius | 
**emoji** | **str** | Emoji representing the weather | 
**background_color** | **int** | A color of the area background in the ARGB format | 

## Example

```python
from tele_rest.models.story_area_type_weather import StoryAreaTypeWeather

# TODO update the JSON string below
json = "{}"
# create an instance of StoryAreaTypeWeather from a JSON string
story_area_type_weather_instance = StoryAreaTypeWeather.from_json(json)
# print the JSON string representation of the object
print(StoryAreaTypeWeather.to_json())

# convert the object into a dict
story_area_type_weather_dict = story_area_type_weather_instance.to_dict()
# create an instance of StoryAreaTypeWeather from a dict
story_area_type_weather_from_dict = StoryAreaTypeWeather.from_dict(story_area_type_weather_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


