# SetChatPhotoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_chat_photo_response import SetChatPhotoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatPhotoResponse from a JSON string
set_chat_photo_response_instance = SetChatPhotoResponse.from_json(json)
# print the JSON string representation of the object
print(SetChatPhotoResponse.to_json())

# convert the object into a dict
set_chat_photo_response_dict = set_chat_photo_response_instance.to_dict()
# create an instance of SetChatPhotoResponse from a dict
set_chat_photo_response_from_dict = SetChatPhotoResponse.from_dict(set_chat_photo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


