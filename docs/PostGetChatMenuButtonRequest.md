# PostGetChatMenuButtonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **int** | Unique identifier for the target private chat. If not specified, default bot&#39;s menu button will be returned | [optional] 

## Example

```python
from tele_rest.models.post_get_chat_menu_button_request import PostGetChatMenuButtonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetChatMenuButtonRequest from a JSON string
post_get_chat_menu_button_request_instance = PostGetChatMenuButtonRequest.from_json(json)
# print the JSON string representation of the object
print(PostGetChatMenuButtonRequest.to_json())

# convert the object into a dict
post_get_chat_menu_button_request_dict = post_get_chat_menu_button_request_instance.to_dict()
# create an instance of PostGetChatMenuButtonRequest from a dict
post_get_chat_menu_button_request_from_dict = PostGetChatMenuButtonRequest.from_dict(post_get_chat_menu_button_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


