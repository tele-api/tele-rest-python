# StoryAreaTypeUniqueGift

Describes a story area pointing to a unique gift. Currently, a story can have at most 1 unique gift area.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the area, always “unique\\_gift” | [default to 'unique_gift']
**name** | **str** | Unique name of the gift | 

## Example

```python
from tele_rest.models.story_area_type_unique_gift import StoryAreaTypeUniqueGift

# TODO update the JSON string below
json = "{}"
# create an instance of StoryAreaTypeUniqueGift from a JSON string
story_area_type_unique_gift_instance = StoryAreaTypeUniqueGift.from_json(json)
# print the JSON string representation of the object
print(StoryAreaTypeUniqueGift.to_json())

# convert the object into a dict
story_area_type_unique_gift_dict = story_area_type_unique_gift_instance.to_dict()
# create an instance of StoryAreaTypeUniqueGift from a dict
story_area_type_unique_gift_from_dict = StoryAreaTypeUniqueGift.from_dict(story_area_type_unique_gift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


