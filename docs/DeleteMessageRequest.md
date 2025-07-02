# DeleteMessageRequest

Request parameters for deleteMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**message_id** | **int** | Identifier of the message to delete | 

## Example

```python
from tele_rest.models.delete_message_request import DeleteMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMessageRequest from a JSON string
delete_message_request_instance = DeleteMessageRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteMessageRequest.to_json())

# convert the object into a dict
delete_message_request_dict = delete_message_request_instance.to_dict()
# create an instance of DeleteMessageRequest from a dict
delete_message_request_from_dict = DeleteMessageRequest.from_dict(delete_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


