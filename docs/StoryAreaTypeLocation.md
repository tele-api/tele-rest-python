# StoryAreaTypeLocation

Describes a story area pointing to a location. Currently, a story can have up to 10 location areas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the area, always “location” | [default to 'location']
**latitude** | **float** | Location latitude in degrees | 
**longitude** | **float** | Location longitude in degrees | 
**address** | [**LocationAddress**](LocationAddress.md) |  | [optional] 

## Example

```python
from tele_rest.models.story_area_type_location import StoryAreaTypeLocation

# TODO update the JSON string below
json = "{}"
# create an instance of StoryAreaTypeLocation from a JSON string
story_area_type_location_instance = StoryAreaTypeLocation.from_json(json)
# print the JSON string representation of the object
print(StoryAreaTypeLocation.to_json())

# convert the object into a dict
story_area_type_location_dict = story_area_type_location_instance.to_dict()
# create an instance of StoryAreaTypeLocation from a dict
story_area_type_location_from_dict = StoryAreaTypeLocation.from_dict(story_area_type_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


