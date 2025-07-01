# LeaveChatPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**LeaveChatPostRequestChatId**](LeaveChatPostRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.leave_chat_post_request import LeaveChatPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveChatPostRequest from a JSON string
leave_chat_post_request_instance = LeaveChatPostRequest.from_json(json)
# print the JSON string representation of the object
print(LeaveChatPostRequest.to_json())

# convert the object into a dict
leave_chat_post_request_dict = leave_chat_post_request_instance.to_dict()
# create an instance of LeaveChatPostRequest from a dict
leave_chat_post_request_from_dict = LeaveChatPostRequest.from_dict(leave_chat_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


