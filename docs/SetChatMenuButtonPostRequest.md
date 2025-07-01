# SetChatMenuButtonPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **int** | Unique identifier for the target private chat. If not specified, default bot&#39;s menu button will be changed | [optional] 
**menu_button** | [**MenuButton**](MenuButton.md) |  | [optional] 

## Example

```python
from tele_rest.models.set_chat_menu_button_post_request import SetChatMenuButtonPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatMenuButtonPostRequest from a JSON string
set_chat_menu_button_post_request_instance = SetChatMenuButtonPostRequest.from_json(json)
# print the JSON string representation of the object
print(SetChatMenuButtonPostRequest.to_json())

# convert the object into a dict
set_chat_menu_button_post_request_dict = set_chat_menu_button_post_request_instance.to_dict()
# create an instance of SetChatMenuButtonPostRequest from a dict
set_chat_menu_button_post_request_from_dict = SetChatMenuButtonPostRequest.from_dict(set_chat_menu_button_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


