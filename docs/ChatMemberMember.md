# ChatMemberMember

Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that has no additional privileges or restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The member&#39;s status in the chat, always “member” | [default to 'member']
**user** | [**User**](User.md) |  | 
**until_date** | **int** | *Optional*. Date when the user&#39;s subscription will expire; Unix time | [optional] 

## Example

```python
from tele_rest.models.chat_member_member import ChatMemberMember

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMemberMember from a JSON string
chat_member_member_instance = ChatMemberMember.from_json(json)
# print the JSON string representation of the object
print(ChatMemberMember.to_json())

# convert the object into a dict
chat_member_member_dict = chat_member_member_instance.to_dict()
# create an instance of ChatMemberMember from a dict
chat_member_member_from_dict = ChatMemberMember.from_dict(chat_member_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


