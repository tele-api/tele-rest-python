# DeleteChatStickerSetRequest

Request parameters for deleteChatStickerSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberRequestChatId**](RestrictChatMemberRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.delete_chat_sticker_set_request import DeleteChatStickerSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteChatStickerSetRequest from a JSON string
delete_chat_sticker_set_request_instance = DeleteChatStickerSetRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteChatStickerSetRequest.to_json())

# convert the object into a dict
delete_chat_sticker_set_request_dict = delete_chat_sticker_set_request_instance.to_dict()
# create an instance of DeleteChatStickerSetRequest from a dict
delete_chat_sticker_set_request_from_dict = DeleteChatStickerSetRequest.from_dict(delete_chat_sticker_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


