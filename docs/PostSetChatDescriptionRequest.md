# PostSetChatDescriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**description** | **str** | New chat description, 0-255 characters | [optional] 

## Example

```python
from tele_rest.models.post_set_chat_description_request import PostSetChatDescriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetChatDescriptionRequest from a JSON string
post_set_chat_description_request_instance = PostSetChatDescriptionRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetChatDescriptionRequest.to_json())

# convert the object into a dict
post_set_chat_description_request_dict = post_set_chat_description_request_instance.to_dict()
# create an instance of PostSetChatDescriptionRequest from a dict
post_set_chat_description_request_from_dict = PostSetChatDescriptionRequest.from_dict(post_set_chat_description_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


