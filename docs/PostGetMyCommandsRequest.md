# PostGetMyCommandsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**BotCommandScope**](BotCommandScope.md) |  | [optional] 
**language_code** | **str** | A two-letter ISO 639-1 language code or an empty string | [optional] 

## Example

```python
from tele_rest.models.post_get_my_commands_request import PostGetMyCommandsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetMyCommandsRequest from a JSON string
post_get_my_commands_request_instance = PostGetMyCommandsRequest.from_json(json)
# print the JSON string representation of the object
print(PostGetMyCommandsRequest.to_json())

# convert the object into a dict
post_get_my_commands_request_dict = post_get_my_commands_request_instance.to_dict()
# create an instance of PostGetMyCommandsRequest from a dict
post_get_my_commands_request_from_dict = PostGetMyCommandsRequest.from_dict(post_get_my_commands_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


