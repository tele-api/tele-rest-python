# GetMyCommandsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[BotCommand]**](BotCommand.md) |  | 

## Example

```python
from tele_rest.models.get_my_commands_response import GetMyCommandsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyCommandsResponse from a JSON string
get_my_commands_response_instance = GetMyCommandsResponse.from_json(json)
# print the JSON string representation of the object
print(GetMyCommandsResponse.to_json())

# convert the object into a dict
get_my_commands_response_dict = get_my_commands_response_instance.to_dict()
# create an instance of GetMyCommandsResponse from a dict
get_my_commands_response_from_dict = GetMyCommandsResponse.from_dict(get_my_commands_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


