# PostSetChatAdministratorCustomTitleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostRestrictChatMemberRequestChatId**](PostRestrictChatMemberRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 
**custom_title** | **str** | New custom title for the administrator; 0-16 characters, emoji are not allowed | 

## Example

```python
from tele_rest.models.post_set_chat_administrator_custom_title_request import PostSetChatAdministratorCustomTitleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetChatAdministratorCustomTitleRequest from a JSON string
post_set_chat_administrator_custom_title_request_instance = PostSetChatAdministratorCustomTitleRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetChatAdministratorCustomTitleRequest.to_json())

# convert the object into a dict
post_set_chat_administrator_custom_title_request_dict = post_set_chat_administrator_custom_title_request_instance.to_dict()
# create an instance of PostSetChatAdministratorCustomTitleRequest from a dict
post_set_chat_administrator_custom_title_request_from_dict = PostSetChatAdministratorCustomTitleRequest.from_dict(post_set_chat_administrator_custom_title_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


