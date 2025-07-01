# ForwardMessagePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of the forum; for forum supergroups only | [optional] 
**from_chat_id** | [**ForwardMessagePostRequestFromChatId**](ForwardMessagePostRequestFromChatId.md) |  | 
**video_start_timestamp** | **int** | New start timestamp for the forwarded video in the message | [optional] 
**disable_notification** | **bool** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the forwarded message from forwarding and saving | [optional] 
**message_id** | **int** | Message identifier in the chat specified in *from\\_chat\\_id* | 

## Example

```python
from tele_rest.models.forward_message_post_request import ForwardMessagePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardMessagePostRequest from a JSON string
forward_message_post_request_instance = ForwardMessagePostRequest.from_json(json)
# print the JSON string representation of the object
print(ForwardMessagePostRequest.to_json())

# convert the object into a dict
forward_message_post_request_dict = forward_message_post_request_instance.to_dict()
# create an instance of ForwardMessagePostRequest from a dict
forward_message_post_request_from_dict = ForwardMessagePostRequest.from_dict(forward_message_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


