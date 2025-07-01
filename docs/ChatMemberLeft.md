# ChatMemberLeft

Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that isn't currently a member of the chat, but may join it themselves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The member&#39;s status in the chat, always “left” | [default to 'left']
**user** | [**User**](User.md) |  | 

## Example

```python
from tele_rest.models.chat_member_left import ChatMemberLeft

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMemberLeft from a JSON string
chat_member_left_instance = ChatMemberLeft.from_json(json)
# print the JSON string representation of the object
print(ChatMemberLeft.to_json())

# convert the object into a dict
chat_member_left_dict = chat_member_left_instance.to_dict()
# create an instance of ChatMemberLeft from a dict
chat_member_left_from_dict = ChatMemberLeft.from_dict(chat_member_left_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


