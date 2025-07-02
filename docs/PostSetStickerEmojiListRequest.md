# PostSetStickerEmojiListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticker** | **str** | File identifier of the sticker | 
**emoji_list** | **List[str]** | A JSON-serialized list of 1-20 emoji associated with the sticker | 

## Example

```python
from tele_rest.models.post_set_sticker_emoji_list_request import PostSetStickerEmojiListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetStickerEmojiListRequest from a JSON string
post_set_sticker_emoji_list_request_instance = PostSetStickerEmojiListRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetStickerEmojiListRequest.to_json())

# convert the object into a dict
post_set_sticker_emoji_list_request_dict = post_set_sticker_emoji_list_request_instance.to_dict()
# create an instance of PostSetStickerEmojiListRequest from a dict
post_set_sticker_emoji_list_request_from_dict = PostSetStickerEmojiListRequest.from_dict(post_set_sticker_emoji_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


