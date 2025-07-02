# DeleteStoryRequest

Request parameters for deleteStory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**story_id** | **int** | Unique identifier of the story to delete | 

## Example

```python
from tele_rest.models.delete_story_request import DeleteStoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteStoryRequest from a JSON string
delete_story_request_instance = DeleteStoryRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteStoryRequest.to_json())

# convert the object into a dict
delete_story_request_dict = delete_story_request_instance.to_dict()
# create an instance of DeleteStoryRequest from a dict
delete_story_request_from_dict = DeleteStoryRequest.from_dict(delete_story_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


