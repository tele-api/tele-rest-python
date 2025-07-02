# GetFileRequest

Request parameters for getFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | File identifier to get information about | 

## Example

```python
from tele_rest.models.get_file_request import GetFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetFileRequest from a JSON string
get_file_request_instance = GetFileRequest.from_json(json)
# print the JSON string representation of the object
print(GetFileRequest.to_json())

# convert the object into a dict
get_file_request_dict = get_file_request_instance.to_dict()
# create an instance of GetFileRequest from a dict
get_file_request_from_dict = GetFileRequest.from_dict(get_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


