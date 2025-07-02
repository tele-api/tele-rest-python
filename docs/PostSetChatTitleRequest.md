# PostSetChatTitleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**title** | **str** | New chat title, 1-128 characters | 

## Example

```python
from tele_rest.models.post_set_chat_title_request import PostSetChatTitleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetChatTitleRequest from a JSON string
post_set_chat_title_request_instance = PostSetChatTitleRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetChatTitleRequest.to_json())

# convert the object into a dict
post_set_chat_title_request_dict = post_set_chat_title_request_instance.to_dict()
# create an instance of PostSetChatTitleRequest from a dict
post_set_chat_title_request_from_dict = PostSetChatTitleRequest.from_dict(post_set_chat_title_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


