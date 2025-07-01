# GetChatMenuButtonPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **int** | Unique identifier for the target private chat. If not specified, default bot&#39;s menu button will be returned | [optional] 

## Example

```python
from tele_rest.models.get_chat_menu_button_post_request import GetChatMenuButtonPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatMenuButtonPostRequest from a JSON string
get_chat_menu_button_post_request_instance = GetChatMenuButtonPostRequest.from_json(json)
# print the JSON string representation of the object
print(GetChatMenuButtonPostRequest.to_json())

# convert the object into a dict
get_chat_menu_button_post_request_dict = get_chat_menu_button_post_request_instance.to_dict()
# create an instance of GetChatMenuButtonPostRequest from a dict
get_chat_menu_button_post_request_from_dict = GetChatMenuButtonPostRequest.from_dict(get_chat_menu_button_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


