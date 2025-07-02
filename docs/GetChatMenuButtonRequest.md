# GetChatMenuButtonRequest

Request parameters for getChatMenuButton

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **int** | Unique identifier for the target private chat. If not specified, default bot&#39;s menu button will be returned | [optional] 

## Example

```python
from tele_rest.models.get_chat_menu_button_request import GetChatMenuButtonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatMenuButtonRequest from a JSON string
get_chat_menu_button_request_instance = GetChatMenuButtonRequest.from_json(json)
# print the JSON string representation of the object
print(GetChatMenuButtonRequest.to_json())

# convert the object into a dict
get_chat_menu_button_request_dict = get_chat_menu_button_request_instance.to_dict()
# create an instance of GetChatMenuButtonRequest from a dict
get_chat_menu_button_request_from_dict = GetChatMenuButtonRequest.from_dict(get_chat_menu_button_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


