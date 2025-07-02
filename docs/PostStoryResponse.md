# PostStoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Story**](Story.md) |  | 

## Example

```python
from tele_rest.models.post_story_response import PostStoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostStoryResponse from a JSON string
post_story_response_instance = PostStoryResponse.from_json(json)
# print the JSON string representation of the object
print(PostStoryResponse.to_json())

# convert the object into a dict
post_story_response_dict = post_story_response_instance.to_dict()
# create an instance of PostStoryResponse from a dict
post_story_response_from_dict = PostStoryResponse.from_dict(post_story_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


