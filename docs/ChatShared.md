# ChatShared

This object contains information about a chat that was shared with the bot using a [KeyboardButtonRequestChat](https://core.telegram.org/bots/api/#keyboardbuttonrequestchat) button.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **int** | Identifier of the request | 
**chat_id** | **int** | Identifier of the shared chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not have access to the chat and could be unable to use this identifier, unless the chat is already known to the bot by some other means. | 
**title** | **str** | *Optional*. Title of the chat, if the title was requested by the bot. | [optional] 
**username** | **str** | *Optional*. Username of the chat, if the username was requested by the bot and available. | [optional] 
**photo** | [**List[PhotoSize]**](PhotoSize.md) | *Optional*. Available sizes of the chat photo, if the photo was requested by the bot | [optional] 

## Example

```python
from tele_rest.models.chat_shared import ChatShared

# TODO update the JSON string below
json = "{}"
# create an instance of ChatShared from a JSON string
chat_shared_instance = ChatShared.from_json(json)
# print the JSON string representation of the object
print(ChatShared.to_json())

# convert the object into a dict
chat_shared_dict = chat_shared_instance.to_dict()
# create an instance of ChatShared from a dict
chat_shared_from_dict = ChatShared.from_dict(chat_shared_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


