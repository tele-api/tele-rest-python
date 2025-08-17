# SetChatAdministratorCustomTitleRequest

Request parameters for setChatAdministratorCustomTitle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberRequestChatId**](RestrictChatMemberRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 
**custom_title** | **str** | New custom title for the administrator; 0-16 characters, emoji are not allowed | 

## Example

```python
from tele_rest.models.set_chat_administrator_custom_title_request import SetChatAdministratorCustomTitleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatAdministratorCustomTitleRequest from a JSON string
set_chat_administrator_custom_title_request_instance = SetChatAdministratorCustomTitleRequest.from_json(json)
# print the JSON string representation of the object
print(SetChatAdministratorCustomTitleRequest.to_json())

# convert the object into a dict
set_chat_administrator_custom_title_request_dict = set_chat_administrator_custom_title_request_instance.to_dict()
# create an instance of SetChatAdministratorCustomTitleRequest from a dict
set_chat_administrator_custom_title_request_from_dict = SetChatAdministratorCustomTitleRequest.from_dict(set_chat_administrator_custom_title_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


