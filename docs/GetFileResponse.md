# GetFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**File**](File.md) |  | 

## Example

```python
from tele_rest.models.get_file_response import GetFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFileResponse from a JSON string
get_file_response_instance = GetFileResponse.from_json(json)
# print the JSON string representation of the object
print(GetFileResponse.to_json())

# convert the object into a dict
get_file_response_dict = get_file_response_instance.to_dict()
# create an instance of GetFileResponse from a dict
get_file_response_from_dict = GetFileResponse.from_dict(get_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


