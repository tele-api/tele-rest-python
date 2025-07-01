# SendContactPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be sent | [optional] 
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of the forum; for forum supergroups only | [optional] 
**phone_number** | **str** | Contact&#39;s phone number | 
**first_name** | **str** | Contact&#39;s first name | 
**last_name** | **str** | Contact&#39;s last name | [optional] 
**vcard** | **str** | Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes | [optional] 
**disable_notification** | **bool** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the sent message from forwarding and saving | [optional] 
**allow_paid_broadcast** | **bool** | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot&#39;s balance | [optional] 
**message_effect_id** | **str** | Unique identifier of the message effect to be added to the message; for private chats only | [optional] 
**reply_parameters** | [**ReplyParameters**](ReplyParameters.md) |  | [optional] 
**reply_markup** | [**SendMessagePostRequestReplyMarkup**](SendMessagePostRequestReplyMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.send_contact_post_request import SendContactPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendContactPostRequest from a JSON string
send_contact_post_request_instance = SendContactPostRequest.from_json(json)
# print the JSON string representation of the object
print(SendContactPostRequest.to_json())

# convert the object into a dict
send_contact_post_request_dict = send_contact_post_request_instance.to_dict()
# create an instance of SendContactPostRequest from a dict
send_contact_post_request_from_dict = SendContactPostRequest.from_dict(send_contact_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


