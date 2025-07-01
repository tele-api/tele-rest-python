# DeleteMessagesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**message_ids** | **List[int]** | A JSON-serialized list of 1-100 identifiers of messages to delete. See [deleteMessage](https://core.telegram.org/bots/api/#deletemessage) for limitations on which messages can be deleted | 

## Example

```python
from tele_rest.models.delete_messages_post_request import DeleteMessagesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMessagesPostRequest from a JSON string
delete_messages_post_request_instance = DeleteMessagesPostRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteMessagesPostRequest.to_json())

# convert the object into a dict
delete_messages_post_request_dict = delete_messages_post_request_instance.to_dict()
# create an instance of DeleteMessagesPostRequest from a dict
delete_messages_post_request_from_dict = DeleteMessagesPostRequest.from_dict(delete_messages_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


