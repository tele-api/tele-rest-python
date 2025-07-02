# LeaveChatRequest

Request parameters for leaveChat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**LeaveChatRequestChatId**](LeaveChatRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.leave_chat_request import LeaveChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveChatRequest from a JSON string
leave_chat_request_instance = LeaveChatRequest.from_json(json)
# print the JSON string representation of the object
print(LeaveChatRequest.to_json())

# convert the object into a dict
leave_chat_request_dict = leave_chat_request_instance.to_dict()
# create an instance of LeaveChatRequest from a dict
leave_chat_request_from_dict = LeaveChatRequest.from_dict(leave_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


