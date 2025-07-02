# PostSetChatMenuButtonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **int** | Unique identifier for the target private chat. If not specified, default bot&#39;s menu button will be changed | [optional] 
**menu_button** | [**MenuButton**](MenuButton.md) |  | [optional] 

## Example

```python
from tele_rest.models.post_set_chat_menu_button_request import PostSetChatMenuButtonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetChatMenuButtonRequest from a JSON string
post_set_chat_menu_button_request_instance = PostSetChatMenuButtonRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetChatMenuButtonRequest.to_json())

# convert the object into a dict
post_set_chat_menu_button_request_dict = post_set_chat_menu_button_request_instance.to_dict()
# create an instance of PostSetChatMenuButtonRequest from a dict
post_set_chat_menu_button_request_from_dict = PostSetChatMenuButtonRequest.from_dict(post_set_chat_menu_button_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


