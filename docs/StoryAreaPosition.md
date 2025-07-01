# StoryAreaPosition

Describes the position of a clickable area within a story.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_percentage** | **float** | The abscissa of the area&#39;s center, as a percentage of the media width | 
**y_percentage** | **float** | The ordinate of the area&#39;s center, as a percentage of the media height | 
**width_percentage** | **float** | The width of the area&#39;s rectangle, as a percentage of the media width | 
**height_percentage** | **float** | The height of the area&#39;s rectangle, as a percentage of the media height | 
**rotation_angle** | **float** | The clockwise rotation angle of the rectangle, in degrees; 0-360 | 
**corner_radius_percentage** | **float** | The radius of the rectangle corner rounding, as a percentage of the media width | 

## Example

```python
from tele_rest.models.story_area_position import StoryAreaPosition

# TODO update the JSON string below
json = "{}"
# create an instance of StoryAreaPosition from a JSON string
story_area_position_instance = StoryAreaPosition.from_json(json)
# print the JSON string representation of the object
print(StoryAreaPosition.to_json())

# convert the object into a dict
story_area_position_dict = story_area_position_instance.to_dict()
# create an instance of StoryAreaPosition from a dict
story_area_position_from_dict = StoryAreaPosition.from_dict(story_area_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


