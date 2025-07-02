# DeleteMyCommandsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.delete_my_commands_response import DeleteMyCommandsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMyCommandsResponse from a JSON string
delete_my_commands_response_instance = DeleteMyCommandsResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteMyCommandsResponse.to_json())

# convert the object into a dict
delete_my_commands_response_dict = delete_my_commands_response_instance.to_dict()
# create an instance of DeleteMyCommandsResponse from a dict
delete_my_commands_response_from_dict = DeleteMyCommandsResponse.from_dict(delete_my_commands_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


