# GetChatAdministratorsRequest

Request parameters for getChatAdministrators

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**GetChatRequestChatId**](GetChatRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.get_chat_administrators_request import GetChatAdministratorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatAdministratorsRequest from a JSON string
get_chat_administrators_request_instance = GetChatAdministratorsRequest.from_json(json)
# print the JSON string representation of the object
print(GetChatAdministratorsRequest.to_json())

# convert the object into a dict
get_chat_administrators_request_dict = get_chat_administrators_request_instance.to_dict()
# create an instance of GetChatAdministratorsRequest from a dict
get_chat_administrators_request_from_dict = GetChatAdministratorsRequest.from_dict(get_chat_administrators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


