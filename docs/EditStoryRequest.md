# EditStoryRequest

Request parameters for editStory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**story_id** | **int** | Unique identifier of the story to edit | 
**content** | [**InputStoryContent**](InputStoryContent.md) |  | 
**caption** | **str** | Caption of the story, 0-2048 characters after entities parsing | [optional] 
**parse_mode** | **str** | Mode for parsing entities in the story caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**areas** | [**List[StoryArea]**](StoryArea.md) | A JSON-serialized list of clickable areas to be shown on the story | [optional] 

## Example

```python
from tele_rest.models.edit_story_request import EditStoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditStoryRequest from a JSON string
edit_story_request_instance = EditStoryRequest.from_json(json)
# print the JSON string representation of the object
print(EditStoryRequest.to_json())

# convert the object into a dict
edit_story_request_dict = edit_story_request_instance.to_dict()
# create an instance of EditStoryRequest from a dict
edit_story_request_from_dict = EditStoryRequest.from_dict(edit_story_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


