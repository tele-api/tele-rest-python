# PostDeleteStoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**story_id** | **int** | Unique identifier of the story to delete | 

## Example

```python
from tele_rest.models.post_delete_story_request import PostDeleteStoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteStoryRequest from a JSON string
post_delete_story_request_instance = PostDeleteStoryRequest.from_json(json)
# print the JSON string representation of the object
print(PostDeleteStoryRequest.to_json())

# convert the object into a dict
post_delete_story_request_dict = post_delete_story_request_instance.to_dict()
# create an instance of PostDeleteStoryRequest from a dict
post_delete_story_request_from_dict = PostDeleteStoryRequest.from_dict(post_delete_story_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


