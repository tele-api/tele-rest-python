# PostGetCustomEmojiStickersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_emoji_ids** | **List[str]** | A JSON-serialized list of custom emoji identifiers. At most 200 custom emoji identifiers can be specified. | 

## Example

```python
from tele_rest.models.post_get_custom_emoji_stickers_request import PostGetCustomEmojiStickersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetCustomEmojiStickersRequest from a JSON string
post_get_custom_emoji_stickers_request_instance = PostGetCustomEmojiStickersRequest.from_json(json)
# print the JSON string representation of the object
print(PostGetCustomEmojiStickersRequest.to_json())

# convert the object into a dict
post_get_custom_emoji_stickers_request_dict = post_get_custom_emoji_stickers_request_instance.to_dict()
# create an instance of PostGetCustomEmojiStickersRequest from a dict
post_get_custom_emoji_stickers_request_from_dict = PostGetCustomEmojiStickersRequest.from_dict(post_get_custom_emoji_stickers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


