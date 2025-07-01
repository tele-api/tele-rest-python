# GetCustomEmojiStickersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_emoji_ids** | **List[str]** | A JSON-serialized list of custom emoji identifiers. At most 200 custom emoji identifiers can be specified. | 

## Example

```python
from tele_rest.models.get_custom_emoji_stickers_post_request import GetCustomEmojiStickersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomEmojiStickersPostRequest from a JSON string
get_custom_emoji_stickers_post_request_instance = GetCustomEmojiStickersPostRequest.from_json(json)
# print the JSON string representation of the object
print(GetCustomEmojiStickersPostRequest.to_json())

# convert the object into a dict
get_custom_emoji_stickers_post_request_dict = get_custom_emoji_stickers_post_request_instance.to_dict()
# create an instance of GetCustomEmojiStickersPostRequest from a dict
get_custom_emoji_stickers_post_request_from_dict = GetCustomEmojiStickersPostRequest.from_dict(get_custom_emoji_stickers_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


