# SetStickerEmojiListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_sticker_emoji_list_response import SetStickerEmojiListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetStickerEmojiListResponse from a JSON string
set_sticker_emoji_list_response_instance = SetStickerEmojiListResponse.from_json(json)
# print the JSON string representation of the object
print(SetStickerEmojiListResponse.to_json())

# convert the object into a dict
set_sticker_emoji_list_response_dict = set_sticker_emoji_list_response_instance.to_dict()
# create an instance of SetStickerEmojiListResponse from a dict
set_sticker_emoji_list_response_from_dict = SetStickerEmojiListResponse.from_dict(set_sticker_emoji_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


