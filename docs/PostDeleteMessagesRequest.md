# PostDeleteMessagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**message_ids** | **List[int]** | A JSON-serialized list of 1-100 identifiers of messages to delete. See [deleteMessage](https://core.telegram.org/bots/api/#deletemessage) for limitations on which messages can be deleted | 

## Example

```python
from tele_rest.models.post_delete_messages_request import PostDeleteMessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteMessagesRequest from a JSON string
post_delete_messages_request_instance = PostDeleteMessagesRequest.from_json(json)
# print the JSON string representation of the object
print(PostDeleteMessagesRequest.to_json())

# convert the object into a dict
post_delete_messages_request_dict = post_delete_messages_request_instance.to_dict()
# create an instance of PostDeleteMessagesRequest from a dict
post_delete_messages_request_from_dict = PostDeleteMessagesRequest.from_dict(post_delete_messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


