# Story

This object represents a story.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**Chat**](Chat.md) |  | 
**id** | **int** | Unique identifier for the story in the chat | 

## Example

```python
from tele_rest.models.story import Story

# TODO update the JSON string below
json = "{}"
# create an instance of Story from a JSON string
story_instance = Story.from_json(json)
# print the JSON string representation of the object
print(Story.to_json())

# convert the object into a dict
story_dict = story_instance.to_dict()
# create an instance of Story from a dict
story_from_dict = Story.from_dict(story_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


