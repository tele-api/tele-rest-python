# DeleteMyCommandsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**BotCommandScope**](BotCommandScope.md) |  | [optional] 
**language_code** | **str** | A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands | [optional] 

## Example

```python
from tele_rest.models.delete_my_commands_post_request import DeleteMyCommandsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMyCommandsPostRequest from a JSON string
delete_my_commands_post_request_instance = DeleteMyCommandsPostRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteMyCommandsPostRequest.to_json())

# convert the object into a dict
delete_my_commands_post_request_dict = delete_my_commands_post_request_instance.to_dict()
# create an instance of DeleteMyCommandsPostRequest from a dict
delete_my_commands_post_request_from_dict = DeleteMyCommandsPostRequest.from_dict(delete_my_commands_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


