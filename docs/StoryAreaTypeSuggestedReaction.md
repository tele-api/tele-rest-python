# StoryAreaTypeSuggestedReaction

Describes a story area pointing to a suggested reaction. Currently, a story can have up to 5 suggested reaction areas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the area, always “suggested\\_reaction” | [default to 'suggested_reaction']
**reaction_type** | [**ReactionType**](ReactionType.md) |  | 
**is_dark** | **bool** | *Optional*. Pass *True* if the reaction area has a dark background | [optional] 
**is_flipped** | **bool** | *Optional*. Pass *True* if reaction area corner is flipped | [optional] 

## Example

```python
from tele_rest.models.story_area_type_suggested_reaction import StoryAreaTypeSuggestedReaction

# TODO update the JSON string below
json = "{}"
# create an instance of StoryAreaTypeSuggestedReaction from a JSON string
story_area_type_suggested_reaction_instance = StoryAreaTypeSuggestedReaction.from_json(json)
# print the JSON string representation of the object
print(StoryAreaTypeSuggestedReaction.to_json())

# convert the object into a dict
story_area_type_suggested_reaction_dict = story_area_type_suggested_reaction_instance.to_dict()
# create an instance of StoryAreaTypeSuggestedReaction from a dict
story_area_type_suggested_reaction_from_dict = StoryAreaTypeSuggestedReaction.from_dict(story_area_type_suggested_reaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


