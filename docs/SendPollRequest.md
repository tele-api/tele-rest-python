# SendPollRequest

Request parameters for sendPoll

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be sent | [optional] 
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of the forum; for forum supergroups only | [optional] 
**question** | **str** | Poll question, 1-300 characters | 
**question_parse_mode** | **str** | Mode for parsing entities in the question. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. Currently, only custom emoji entities are allowed | [optional] 
**question_entities** | [**List[MessageEntity]**](MessageEntity.md) | A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of *question\\_parse\\_mode* | [optional] 
**options** | [**List[InputPollOption]**](InputPollOption.md) | A JSON-serialized list of 2-10 answer options | 
**is_anonymous** | **bool** | *True*, if the poll needs to be anonymous, defaults to *True* | [optional] 
**type** | **str** | Poll type, “quiz” or “regular”, defaults to “regular” | [optional] 
**allows_multiple_answers** | **bool** | *True*, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to *False* | [optional] 
**correct_option_id** | **int** | 0-based identifier of the correct answer option, required for polls in quiz mode | [optional] 
**explanation** | **str** | Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing | [optional] 
**explanation_parse_mode** | **str** | Mode for parsing entities in the explanation. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**explanation_entities** | [**List[MessageEntity]**](MessageEntity.md) | A JSON-serialized list of special entities that appear in the poll explanation. It can be specified instead of *explanation\\_parse\\_mode* | [optional] 
**open_period** | **int** | Amount of time in seconds the poll will be active after creation, 5-600. Can&#39;t be used together with *close\\_date*. | [optional] 
**close_date** | **int** | Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can&#39;t be used together with *open\\_period*. | [optional] 
**is_closed** | **bool** | Pass *True* if the poll needs to be immediately closed. This can be useful for poll preview. | [optional] 
**disable_notification** | **bool** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the sent message from forwarding and saving | [optional] 
**allow_paid_broadcast** | **bool** | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot&#39;s balance | [optional] 
**message_effect_id** | **str** | Unique identifier of the message effect to be added to the message; for private chats only | [optional] 
**reply_parameters** | [**ReplyParameters**](ReplyParameters.md) |  | [optional] 
**reply_markup** | [**SendMessageRequestReplyMarkup**](SendMessageRequestReplyMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.send_poll_request import SendPollRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendPollRequest from a JSON string
send_poll_request_instance = SendPollRequest.from_json(json)
# print the JSON string representation of the object
print(SendPollRequest.to_json())

# convert the object into a dict
send_poll_request_dict = send_poll_request_instance.to_dict()
# create an instance of SendPollRequest from a dict
send_poll_request_from_dict = SendPollRequest.from_dict(send_poll_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


