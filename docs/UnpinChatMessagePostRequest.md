# UnpinChatMessagePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be unpinned | [optional] 
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**message_id** | **int** | Identifier of the message to unpin. Required if *business\\_connection\\_id* is specified. If not specified, the most recent pinned message (by sending date) will be unpinned. | [optional] 

## Example

```python
from tele_rest.models.unpin_chat_message_post_request import UnpinChatMessagePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnpinChatMessagePostRequest from a JSON string
unpin_chat_message_post_request_instance = UnpinChatMessagePostRequest.from_json(json)
# print the JSON string representation of the object
print(UnpinChatMessagePostRequest.to_json())

# convert the object into a dict
unpin_chat_message_post_request_dict = unpin_chat_message_post_request_instance.to_dict()
# create an instance of UnpinChatMessagePostRequest from a dict
unpin_chat_message_post_request_from_dict = UnpinChatMessagePostRequest.from_dict(unpin_chat_message_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


