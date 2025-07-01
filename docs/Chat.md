# Chat

This object represents a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. | 
**type** | **str** | Type of the chat, can be either “private”, “group”, “supergroup” or “channel” | 
**title** | **str** | *Optional*. Title, for supergroups, channels and group chats | [optional] 
**username** | **str** | *Optional*. Username, for private chats, supergroups and channels if available | [optional] 
**first_name** | **str** | *Optional*. First name of the other party in a private chat | [optional] 
**last_name** | **str** | *Optional*. Last name of the other party in a private chat | [optional] 
**is_forum** | **bool** | *Optional*. *True*, if the supergroup chat is a forum (has [topics](https://telegram.org/blog/topics-in-groups-collectible-usernames#topics-in-groups) enabled) | [optional] [default to True]

## Example

```python
from tele_rest.models.chat import Chat

# TODO update the JSON string below
json = "{}"
# create an instance of Chat from a JSON string
chat_instance = Chat.from_json(json)
# print the JSON string representation of the object
print(Chat.to_json())

# convert the object into a dict
chat_dict = chat_instance.to_dict()
# create an instance of Chat from a dict
chat_from_dict = Chat.from_dict(chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


