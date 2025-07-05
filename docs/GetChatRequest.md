# GetChatRequest

Request parameters for getChat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**LeaveChatRequestChatId**](LeaveChatRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.get_chat_request import GetChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatRequest from a JSON string
get_chat_request_instance = GetChatRequest.from_json(json)
# print the JSON string representation of the object
print(GetChatRequest.to_json())

# convert the object into a dict
get_chat_request_dict = get_chat_request_instance.to_dict()
# create an instance of GetChatRequest from a dict
get_chat_request_from_dict = GetChatRequest.from_dict(get_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


