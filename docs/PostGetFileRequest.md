# PostGetFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | File identifier to get information about | 

## Example

```python
from tele_rest.models.post_get_file_request import PostGetFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetFileRequest from a JSON string
post_get_file_request_instance = PostGetFileRequest.from_json(json)
# print the JSON string representation of the object
print(PostGetFileRequest.to_json())

# convert the object into a dict
post_get_file_request_dict = post_get_file_request_instance.to_dict()
# create an instance of PostGetFileRequest from a dict
post_get_file_request_from_dict = PostGetFileRequest.from_dict(post_get_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


