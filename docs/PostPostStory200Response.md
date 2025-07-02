# PostPostStory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Story**](Story.md) |  | 

## Example

```python
from tele_rest.models.post_post_story200_response import PostPostStory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostPostStory200Response from a JSON string
post_post_story200_response_instance = PostPostStory200Response.from_json(json)
# print the JSON string representation of the object
print(PostPostStory200Response.to_json())

# convert the object into a dict
post_post_story200_response_dict = post_post_story200_response_instance.to_dict()
# create an instance of PostPostStory200Response from a dict
post_post_story200_response_from_dict = PostPostStory200Response.from_dict(post_post_story200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


