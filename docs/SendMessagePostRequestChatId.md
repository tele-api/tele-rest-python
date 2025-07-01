# SendMessagePostRequestChatId

Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.send_message_post_request_chat_id import SendMessagePostRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessagePostRequestChatId from a JSON string
send_message_post_request_chat_id_instance = SendMessagePostRequestChatId.from_json(json)
# print the JSON string representation of the object
print(SendMessagePostRequestChatId.to_json())

# convert the object into a dict
send_message_post_request_chat_id_dict = send_message_post_request_chat_id_instance.to_dict()
# create an instance of SendMessagePostRequestChatId from a dict
send_message_post_request_chat_id_from_dict = SendMessagePostRequestChatId.from_dict(send_message_post_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


