# SendGiftPostRequestChatId

Required if *user\\_id* is not specified. Unique identifier for the chat or username of the channel (in the format `@channelusername`) that will receive the gift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.send_gift_post_request_chat_id import SendGiftPostRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of SendGiftPostRequestChatId from a JSON string
send_gift_post_request_chat_id_instance = SendGiftPostRequestChatId.from_json(json)
# print the JSON string representation of the object
print(SendGiftPostRequestChatId.to_json())

# convert the object into a dict
send_gift_post_request_chat_id_dict = send_gift_post_request_chat_id_instance.to_dict()
# create an instance of SendGiftPostRequestChatId from a dict
send_gift_post_request_chat_id_from_dict = SendGiftPostRequestChatId.from_dict(send_gift_post_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


