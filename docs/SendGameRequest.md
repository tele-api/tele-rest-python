# SendGameRequest

Request parameters for sendGame

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be sent | [optional] 
**chat_id** | **int** | Unique identifier for the target chat. Games can&#39;t be sent to channel direct messages chats and channel chats. | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only | [optional] 
**game_short_name** | **str** | Short name of the game, serves as the unique identifier for the game. Set up your games via [@BotFather](https://t.me/botfather). | 
**disable_notification** | **bool** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the sent message from forwarding and saving | [optional] 
**allow_paid_broadcast** | **bool** | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot&#39;s balance | [optional] 
**message_effect_id** | **str** | Unique identifier of the message effect to be added to the message; for private chats only | [optional] 
**reply_parameters** | [**ReplyParameters**](ReplyParameters.md) |  | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.send_game_request import SendGameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendGameRequest from a JSON string
send_game_request_instance = SendGameRequest.from_json(json)
# print the JSON string representation of the object
print(SendGameRequest.to_json())

# convert the object into a dict
send_game_request_dict = send_game_request_instance.to_dict()
# create an instance of SendGameRequest from a dict
send_game_request_from_dict = SendGameRequest.from_dict(send_game_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


