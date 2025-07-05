# DeleteStoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.delete_story_response import DeleteStoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteStoryResponse from a JSON string
delete_story_response_instance = DeleteStoryResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteStoryResponse.to_json())

# convert the object into a dict
delete_story_response_dict = delete_story_response_instance.to_dict()
# create an instance of DeleteStoryResponse from a dict
delete_story_response_from_dict = DeleteStoryResponse.from_dict(delete_story_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


