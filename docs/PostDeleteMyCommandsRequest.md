# PostDeleteMyCommandsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**BotCommandScope**](BotCommandScope.md) |  | [optional] 
**language_code** | **str** | A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands | [optional] 

## Example

```python
from tele_rest.models.post_delete_my_commands_request import PostDeleteMyCommandsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteMyCommandsRequest from a JSON string
post_delete_my_commands_request_instance = PostDeleteMyCommandsRequest.from_json(json)
# print the JSON string representation of the object
print(PostDeleteMyCommandsRequest.to_json())

# convert the object into a dict
post_delete_my_commands_request_dict = post_delete_my_commands_request_instance.to_dict()
# create an instance of PostDeleteMyCommandsRequest from a dict
post_delete_my_commands_request_from_dict = PostDeleteMyCommandsRequest.from_dict(post_delete_my_commands_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


