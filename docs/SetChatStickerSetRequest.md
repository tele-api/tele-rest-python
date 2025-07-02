# SetChatStickerSetRequest

Request parameters for setChatStickerSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**BotCommandScopeChatChatId**](BotCommandScopeChatChatId.md) |  | 
**sticker_set_name** | **str** | Name of the sticker set to be set as the group sticker set | 

## Example

```python
from tele_rest.models.set_chat_sticker_set_request import SetChatStickerSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatStickerSetRequest from a JSON string
set_chat_sticker_set_request_instance = SetChatStickerSetRequest.from_json(json)
# print the JSON string representation of the object
print(SetChatStickerSetRequest.to_json())

# convert the object into a dict
set_chat_sticker_set_request_dict = set_chat_sticker_set_request_instance.to_dict()
# create an instance of SetChatStickerSetRequest from a dict
set_chat_sticker_set_request_from_dict = SetChatStickerSetRequest.from_dict(set_chat_sticker_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


