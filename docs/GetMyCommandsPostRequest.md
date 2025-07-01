# GetMyCommandsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**BotCommandScope**](BotCommandScope.md) |  | [optional] 
**language_code** | **str** | A two-letter ISO 639-1 language code or an empty string | [optional] 

## Example

```python
from tele_rest.models.get_my_commands_post_request import GetMyCommandsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyCommandsPostRequest from a JSON string
get_my_commands_post_request_instance = GetMyCommandsPostRequest.from_json(json)
# print the JSON string representation of the object
print(GetMyCommandsPostRequest.to_json())

# convert the object into a dict
get_my_commands_post_request_dict = get_my_commands_post_request_instance.to_dict()
# create an instance of GetMyCommandsPostRequest from a dict
get_my_commands_post_request_from_dict = GetMyCommandsPostRequest.from_dict(get_my_commands_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


