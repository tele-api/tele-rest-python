# DeleteChatStickerSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.delete_chat_sticker_set_response import DeleteChatStickerSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteChatStickerSetResponse from a JSON string
delete_chat_sticker_set_response_instance = DeleteChatStickerSetResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteChatStickerSetResponse.to_json())

# convert the object into a dict
delete_chat_sticker_set_response_dict = delete_chat_sticker_set_response_instance.to_dict()
# create an instance of DeleteChatStickerSetResponse from a dict
delete_chat_sticker_set_response_from_dict = DeleteChatStickerSetResponse.from_dict(delete_chat_sticker_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


