# PostStoryPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Story**](Story.md) |  | 

## Example

```python
from tele_rest.models.post_story_post200_response import PostStoryPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostStoryPost200Response from a JSON string
post_story_post200_response_instance = PostStoryPost200Response.from_json(json)
# print the JSON string representation of the object
print(PostStoryPost200Response.to_json())

# convert the object into a dict
post_story_post200_response_dict = post_story_post200_response_instance.to_dict()
# create an instance of PostStoryPost200Response from a dict
post_story_post200_response_from_dict = PostStoryPost200Response.from_dict(post_story_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


