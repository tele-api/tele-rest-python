# PostSetMyCommandsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | [**List[BotCommand]**](BotCommand.md) | A JSON-serialized list of bot commands to be set as the list of the bot&#39;s commands. At most 100 commands can be specified. | 
**scope** | [**BotCommandScope**](BotCommandScope.md) |  | [optional] 
**language_code** | **str** | A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands | [optional] 

## Example

```python
from tele_rest.models.post_set_my_commands_request import PostSetMyCommandsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetMyCommandsRequest from a JSON string
post_set_my_commands_request_instance = PostSetMyCommandsRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetMyCommandsRequest.to_json())

# convert the object into a dict
post_set_my_commands_request_dict = post_set_my_commands_request_instance.to_dict()
# create an instance of PostSetMyCommandsRequest from a dict
post_set_my_commands_request_from_dict = PostSetMyCommandsRequest.from_dict(post_set_my_commands_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


