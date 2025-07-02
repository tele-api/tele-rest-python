# PostVerifyChatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**custom_description** | **str** | Custom description for the verification; 0-70 characters. Must be empty if the organization isn&#39;t allowed to provide a custom verification description. | [optional] 

## Example

```python
from tele_rest.models.post_verify_chat_request import PostVerifyChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostVerifyChatRequest from a JSON string
post_verify_chat_request_instance = PostVerifyChatRequest.from_json(json)
# print the JSON string representation of the object
print(PostVerifyChatRequest.to_json())

# convert the object into a dict
post_verify_chat_request_dict = post_verify_chat_request_instance.to_dict()
# create an instance of PostVerifyChatRequest from a dict
post_verify_chat_request_from_dict = PostVerifyChatRequest.from_dict(post_verify_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


