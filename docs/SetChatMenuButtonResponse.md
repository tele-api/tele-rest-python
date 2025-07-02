# SetChatMenuButtonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_chat_menu_button_response import SetChatMenuButtonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatMenuButtonResponse from a JSON string
set_chat_menu_button_response_instance = SetChatMenuButtonResponse.from_json(json)
# print the JSON string representation of the object
print(SetChatMenuButtonResponse.to_json())

# convert the object into a dict
set_chat_menu_button_response_dict = set_chat_menu_button_response_instance.to_dict()
# create an instance of SetChatMenuButtonResponse from a dict
set_chat_menu_button_response_from_dict = SetChatMenuButtonResponse.from_dict(set_chat_menu_button_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


