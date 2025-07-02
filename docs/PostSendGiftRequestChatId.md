# PostSendGiftRequestChatId

Required if *user\\_id* is not specified. Unique identifier for the chat or username of the channel (in the format `@channelusername`) that will receive the gift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_send_gift_request_chat_id import PostSendGiftRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendGiftRequestChatId from a JSON string
post_send_gift_request_chat_id_instance = PostSendGiftRequestChatId.from_json(json)
# print the JSON string representation of the object
print(PostSendGiftRequestChatId.to_json())

# convert the object into a dict
post_send_gift_request_chat_id_dict = post_send_gift_request_chat_id_instance.to_dict()
# create an instance of PostSendGiftRequestChatId from a dict
post_send_gift_request_chat_id_from_dict = PostSendGiftRequestChatId.from_dict(post_send_gift_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


