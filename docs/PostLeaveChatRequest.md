# PostLeaveChatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostLeaveChatRequestChatId**](PostLeaveChatRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.post_leave_chat_request import PostLeaveChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLeaveChatRequest from a JSON string
post_leave_chat_request_instance = PostLeaveChatRequest.from_json(json)
# print the JSON string representation of the object
print(PostLeaveChatRequest.to_json())

# convert the object into a dict
post_leave_chat_request_dict = post_leave_chat_request_instance.to_dict()
# create an instance of PostLeaveChatRequest from a dict
post_leave_chat_request_from_dict = PostLeaveChatRequest.from_dict(post_leave_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


