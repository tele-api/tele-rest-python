# PostDeleteMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**message_id** | **int** | Identifier of the message to delete | 

## Example

```python
from tele_rest.models.post_delete_message_request import PostDeleteMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteMessageRequest from a JSON string
post_delete_message_request_instance = PostDeleteMessageRequest.from_json(json)
# print the JSON string representation of the object
print(PostDeleteMessageRequest.to_json())

# convert the object into a dict
post_delete_message_request_dict = post_delete_message_request_instance.to_dict()
# create an instance of PostDeleteMessageRequest from a dict
post_delete_message_request_from_dict = PostDeleteMessageRequest.from_dict(post_delete_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


