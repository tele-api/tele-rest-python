# PostSendPaidMediaRequestChatId

Unique identifier for the target chat or username of the target channel (in the format `@channelusername`). If the chat is a channel, all Telegram Star proceeds from this media will be credited to the chat's balance. Otherwise, they will be credited to the bot's balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_send_paid_media_request_chat_id import PostSendPaidMediaRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendPaidMediaRequestChatId from a JSON string
post_send_paid_media_request_chat_id_instance = PostSendPaidMediaRequestChatId.from_json(json)
# print the JSON string representation of the object
print(PostSendPaidMediaRequestChatId.to_json())

# convert the object into a dict
post_send_paid_media_request_chat_id_dict = post_send_paid_media_request_chat_id_instance.to_dict()
# create an instance of PostSendPaidMediaRequestChatId from a dict
post_send_paid_media_request_chat_id_from_dict = PostSendPaidMediaRequestChatId.from_dict(post_send_paid_media_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


