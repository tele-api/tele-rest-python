# GetMyCommandsRequest

Request parameters for getMyCommands

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**BotCommandScope**](BotCommandScope.md) |  | [optional] 
**language_code** | **str** | A two-letter ISO 639-1 language code or an empty string | [optional] 

## Example

```python
from tele_rest.models.get_my_commands_request import GetMyCommandsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyCommandsRequest from a JSON string
get_my_commands_request_instance = GetMyCommandsRequest.from_json(json)
# print the JSON string representation of the object
print(GetMyCommandsRequest.to_json())

# convert the object into a dict
get_my_commands_request_dict = get_my_commands_request_instance.to_dict()
# create an instance of GetMyCommandsRequest from a dict
get_my_commands_request_from_dict = GetMyCommandsRequest.from_dict(get_my_commands_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


