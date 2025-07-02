# GetChatMenuButtonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**MenuButton**](MenuButton.md) |  | 

## Example

```python
from tele_rest.models.get_chat_menu_button_response import GetChatMenuButtonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatMenuButtonResponse from a JSON string
get_chat_menu_button_response_instance = GetChatMenuButtonResponse.from_json(json)
# print the JSON string representation of the object
print(GetChatMenuButtonResponse.to_json())

# convert the object into a dict
get_chat_menu_button_response_dict = get_chat_menu_button_response_instance.to_dict()
# create an instance of GetChatMenuButtonResponse from a dict
get_chat_menu_button_response_from_dict = GetChatMenuButtonResponse.from_dict(get_chat_menu_button_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


