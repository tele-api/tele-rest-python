# StoryArea

Describes a clickable area on a story media.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | [**StoryAreaPosition**](StoryAreaPosition.md) |  | 
**type** | [**StoryAreaType**](StoryAreaType.md) |  | 

## Example

```python
from tele_rest.models.story_area import StoryArea

# TODO update the JSON string below
json = "{}"
# create an instance of StoryArea from a JSON string
story_area_instance = StoryArea.from_json(json)
# print the JSON string representation of the object
print(StoryArea.to_json())

# convert the object into a dict
story_area_dict = story_area_instance.to_dict()
# create an instance of StoryArea from a dict
story_area_from_dict = StoryArea.from_dict(story_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


