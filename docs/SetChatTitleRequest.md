# SetChatTitleRequest

Request parameters for setChatTitle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**title** | **str** | New chat title, 1-128 characters | 

## Example

```python
from tele_rest.models.set_chat_title_request import SetChatTitleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatTitleRequest from a JSON string
set_chat_title_request_instance = SetChatTitleRequest.from_json(json)
# print the JSON string representation of the object
print(SetChatTitleRequest.to_json())

# convert the object into a dict
set_chat_title_request_dict = set_chat_title_request_instance.to_dict()
# create an instance of SetChatTitleRequest from a dict
set_chat_title_request_from_dict = SetChatTitleRequest.from_dict(set_chat_title_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


