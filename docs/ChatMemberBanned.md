# ChatMemberBanned

Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that was banned in the chat and can't return to the chat or view chat messages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The member&#39;s status in the chat, always “kicked” | [default to 'kicked']
**user** | [**User**](User.md) |  | 
**until_date** | **int** | Date when restrictions will be lifted for this user; Unix time. If 0, then the user is banned forever | 

## Example

```python
from tele_rest.models.chat_member_banned import ChatMemberBanned

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMemberBanned from a JSON string
chat_member_banned_instance = ChatMemberBanned.from_json(json)
# print the JSON string representation of the object
print(ChatMemberBanned.to_json())

# convert the object into a dict
chat_member_banned_dict = chat_member_banned_instance.to_dict()
# create an instance of ChatMemberBanned from a dict
chat_member_banned_from_dict = ChatMemberBanned.from_dict(chat_member_banned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


