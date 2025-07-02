# EditStoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Story**](Story.md) |  | 

## Example

```python
from tele_rest.models.edit_story_response import EditStoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditStoryResponse from a JSON string
edit_story_response_instance = EditStoryResponse.from_json(json)
# print the JSON string representation of the object
print(EditStoryResponse.to_json())

# convert the object into a dict
edit_story_response_dict = edit_story_response_instance.to_dict()
# create an instance of EditStoryResponse from a dict
edit_story_response_from_dict = EditStoryResponse.from_dict(edit_story_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


