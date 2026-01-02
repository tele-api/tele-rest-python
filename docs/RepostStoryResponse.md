# RepostStoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Story**](Story.md) |  | 

## Example

```python
from tele_rest.models.repost_story_response import RepostStoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RepostStoryResponse from a JSON string
repost_story_response_instance = RepostStoryResponse.from_json(json)
# print the JSON string representation of the object
print(RepostStoryResponse.to_json())

# convert the object into a dict
repost_story_response_dict = repost_story_response_instance.to_dict()
# create an instance of RepostStoryResponse from a dict
repost_story_response_from_dict = RepostStoryResponse.from_dict(repost_story_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


