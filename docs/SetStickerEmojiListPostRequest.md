# SetStickerEmojiListPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticker** | **str** | File identifier of the sticker | 
**emoji_list** | **List[str]** | A JSON-serialized list of 1-20 emoji associated with the sticker | 

## Example

```python
from tele_rest.models.set_sticker_emoji_list_post_request import SetStickerEmojiListPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetStickerEmojiListPostRequest from a JSON string
set_sticker_emoji_list_post_request_instance = SetStickerEmojiListPostRequest.from_json(json)
# print the JSON string representation of the object
print(SetStickerEmojiListPostRequest.to_json())

# convert the object into a dict
set_sticker_emoji_list_post_request_dict = set_sticker_emoji_list_post_request_instance.to_dict()
# create an instance of SetStickerEmojiListPostRequest from a dict
set_sticker_emoji_list_post_request_from_dict = SetStickerEmojiListPostRequest.from_dict(set_sticker_emoji_list_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


