# SetChatPhotoRequest

Request parameters for setChatPhoto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**photo** | **object** |  | 

## Example

```python
from tele_rest.models.set_chat_photo_request import SetChatPhotoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatPhotoRequest from a JSON string
set_chat_photo_request_instance = SetChatPhotoRequest.from_json(json)
# print the JSON string representation of the object
print(SetChatPhotoRequest.to_json())

# convert the object into a dict
set_chat_photo_request_dict = set_chat_photo_request_instance.to_dict()
# create an instance of SetChatPhotoRequest from a dict
set_chat_photo_request_from_dict = SetChatPhotoRequest.from_dict(set_chat_photo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


