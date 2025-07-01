# StoryAreaTypeLink

Describes a story area pointing to an HTTP or tg:// link. Currently, a story can have up to 3 link areas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the area, always “link” | [default to 'link']
**url** | **str** | HTTP or tg:// URL to be opened when the area is clicked | 

## Example

```python
from tele_rest.models.story_area_type_link import StoryAreaTypeLink

# TODO update the JSON string below
json = "{}"
# create an instance of StoryAreaTypeLink from a JSON string
story_area_type_link_instance = StoryAreaTypeLink.from_json(json)
# print the JSON string representation of the object
print(StoryAreaTypeLink.to_json())

# convert the object into a dict
story_area_type_link_dict = story_area_type_link_instance.to_dict()
# create an instance of StoryAreaTypeLink from a dict
story_area_type_link_from_dict = StoryAreaTypeLink.from_dict(story_area_type_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


