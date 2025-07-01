# StoryAreaType

Describes the type of a clickable area on a story. Currently, it can be one of  * [StoryAreaTypeLocation](https://core.telegram.org/bots/api/#storyareatypelocation) * [StoryAreaTypeSuggestedReaction](https://core.telegram.org/bots/api/#storyareatypesuggestedreaction) * [StoryAreaTypeLink](https://core.telegram.org/bots/api/#storyareatypelink) * [StoryAreaTypeWeather](https://core.telegram.org/bots/api/#storyareatypeweather) * [StoryAreaTypeUniqueGift](https://core.telegram.org/bots/api/#storyareatypeuniquegift)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the area, always “unique\\_gift” | [default to 'unique_gift']
**latitude** | **float** | Location latitude in degrees | 
**longitude** | **float** | Location longitude in degrees | 
**address** | [**LocationAddress**](LocationAddress.md) |  | [optional] 
**reaction_type** | [**ReactionType**](ReactionType.md) |  | 
**is_dark** | **bool** | *Optional*. Pass *True* if the reaction area has a dark background | [optional] 
**is_flipped** | **bool** | *Optional*. Pass *True* if reaction area corner is flipped | [optional] 
**url** | **str** | HTTP or tg:// URL to be opened when the area is clicked | 
**temperature** | **float** | Temperature, in degree Celsius | 
**emoji** | **str** | Emoji representing the weather | 
**background_color** | **int** | A color of the area background in the ARGB format | 
**name** | **str** | Unique name of the gift | 

## Example

```python
from tele_rest.models.story_area_type import StoryAreaType

# TODO update the JSON string below
json = "{}"
# create an instance of StoryAreaType from a JSON string
story_area_type_instance = StoryAreaType.from_json(json)
# print the JSON string representation of the object
print(StoryAreaType.to_json())

# convert the object into a dict
story_area_type_dict = story_area_type_instance.to_dict()
# create an instance of StoryAreaType from a dict
story_area_type_from_dict = StoryAreaType.from_dict(story_area_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


