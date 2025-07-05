# DeleteChatPhotoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.delete_chat_photo_response import DeleteChatPhotoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteChatPhotoResponse from a JSON string
delete_chat_photo_response_instance = DeleteChatPhotoResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteChatPhotoResponse.to_json())

# convert the object into a dict
delete_chat_photo_response_dict = delete_chat_photo_response_instance.to_dict()
# create an instance of DeleteChatPhotoResponse from a dict
delete_chat_photo_response_from_dict = DeleteChatPhotoResponse.from_dict(delete_chat_photo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


