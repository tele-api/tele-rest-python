# ChatMemberOwner

Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that owns the chat and has all administrator privileges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The member&#39;s status in the chat, always “creator” | [default to 'creator']
**user** | [**User**](User.md) |  | 
**is_anonymous** | **bool** | *True*, if the user&#39;s presence in the chat is hidden | 
**custom_title** | **str** | *Optional*. Custom title for this user | [optional] 

## Example

```python
from tele_rest.models.chat_member_owner import ChatMemberOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMemberOwner from a JSON string
chat_member_owner_instance = ChatMemberOwner.from_json(json)
# print the JSON string representation of the object
print(ChatMemberOwner.to_json())

# convert the object into a dict
chat_member_owner_dict = chat_member_owner_instance.to_dict()
# create an instance of ChatMemberOwner from a dict
chat_member_owner_from_dict = ChatMemberOwner.from_dict(chat_member_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


