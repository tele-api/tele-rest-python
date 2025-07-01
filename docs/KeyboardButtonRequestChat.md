# KeyboardButtonRequestChat

This object defines the criteria used to request a suitable chat. Information about the selected chat will be shared with the bot when the corresponding button is pressed. The bot will be granted requested rights in the chat if appropriate. [More about requesting chats »](https://core.telegram.org/bots/features#chat-and-user-selection).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **int** | Signed 32-bit identifier of the request, which will be received back in the [ChatShared](https://core.telegram.org/bots/api/#chatshared) object. Must be unique within the message | 
**chat_is_channel** | **bool** | Pass *True* to request a channel chat, pass *False* to request a group or a supergroup chat. | 
**chat_is_forum** | **bool** | *Optional*. Pass *True* to request a forum supergroup, pass *False* to request a non-forum chat. If not specified, no additional restrictions are applied. | [optional] 
**chat_has_username** | **bool** | *Optional*. Pass *True* to request a supergroup or a channel with a username, pass *False* to request a chat without a username. If not specified, no additional restrictions are applied. | [optional] 
**chat_is_created** | **bool** | *Optional*. Pass *True* to request a chat owned by the user. Otherwise, no additional restrictions are applied. | [optional] 
**user_administrator_rights** | [**ChatAdministratorRights**](ChatAdministratorRights.md) |  | [optional] 
**bot_administrator_rights** | [**ChatAdministratorRights**](ChatAdministratorRights.md) |  | [optional] 
**bot_is_member** | **bool** | *Optional*. Pass *True* to request a chat with the bot as a member. Otherwise, no additional restrictions are applied. | [optional] 
**request_title** | **bool** | *Optional*. Pass *True* to request the chat&#39;s title | [optional] 
**request_username** | **bool** | *Optional*. Pass *True* to request the chat&#39;s username | [optional] 
**request_photo** | **bool** | *Optional*. Pass *True* to request the chat&#39;s photo | [optional] 

## Example

```python
from tele_rest.models.keyboard_button_request_chat import KeyboardButtonRequestChat

# TODO update the JSON string below
json = "{}"
# create an instance of KeyboardButtonRequestChat from a JSON string
keyboard_button_request_chat_instance = KeyboardButtonRequestChat.from_json(json)
# print the JSON string representation of the object
print(KeyboardButtonRequestChat.to_json())

# convert the object into a dict
keyboard_button_request_chat_dict = keyboard_button_request_chat_instance.to_dict()
# create an instance of KeyboardButtonRequestChat from a dict
keyboard_button_request_chat_from_dict = KeyboardButtonRequestChat.from_dict(keyboard_button_request_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


