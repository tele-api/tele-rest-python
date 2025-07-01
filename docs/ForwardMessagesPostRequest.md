# ForwardMessagesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of the forum; for forum supergroups only | [optional] 
**from_chat_id** | [**ForwardMessagesPostRequestFromChatId**](ForwardMessagesPostRequestFromChatId.md) |  | 
**message_ids** | **List[int]** | A JSON-serialized list of 1-100 identifiers of messages in the chat *from\\_chat\\_id* to forward. The identifiers must be specified in a strictly increasing order. | 
**disable_notification** | **bool** | Sends the messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the forwarded messages from forwarding and saving | [optional] 

## Example

```python
from tele_rest.models.forward_messages_post_request import ForwardMessagesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardMessagesPostRequest from a JSON string
forward_messages_post_request_instance = ForwardMessagesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ForwardMessagesPostRequest.to_json())

# convert the object into a dict
forward_messages_post_request_dict = forward_messages_post_request_instance.to_dict()
# create an instance of ForwardMessagesPostRequest from a dict
forward_messages_post_request_from_dict = ForwardMessagesPostRequest.from_dict(forward_messages_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


