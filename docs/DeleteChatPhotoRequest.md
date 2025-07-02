# DeleteChatPhotoRequest

Request parameters for deleteChatPhoto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.delete_chat_photo_request import DeleteChatPhotoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteChatPhotoRequest from a JSON string
delete_chat_photo_request_instance = DeleteChatPhotoRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteChatPhotoRequest.to_json())

# convert the object into a dict
delete_chat_photo_request_dict = delete_chat_photo_request_instance.to_dict()
# create an instance of DeleteChatPhotoRequest from a dict
delete_chat_photo_request_from_dict = DeleteChatPhotoRequest.from_dict(delete_chat_photo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


