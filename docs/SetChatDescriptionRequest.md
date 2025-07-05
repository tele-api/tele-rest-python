# SetChatDescriptionRequest

Request parameters for setChatDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**description** | **str** | New chat description, 0-255 characters | [optional] 

## Example

```python
from tele_rest.models.set_chat_description_request import SetChatDescriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatDescriptionRequest from a JSON string
set_chat_description_request_instance = SetChatDescriptionRequest.from_json(json)
# print the JSON string representation of the object
print(SetChatDescriptionRequest.to_json())

# convert the object into a dict
set_chat_description_request_dict = set_chat_description_request_instance.to_dict()
# create an instance of SetChatDescriptionRequest from a dict
set_chat_description_request_from_dict = SetChatDescriptionRequest.from_dict(set_chat_description_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


