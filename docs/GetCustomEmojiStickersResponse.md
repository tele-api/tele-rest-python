# GetCustomEmojiStickersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[Sticker]**](Sticker.md) |  | 

## Example

```python
from tele_rest.models.get_custom_emoji_stickers_response import GetCustomEmojiStickersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomEmojiStickersResponse from a JSON string
get_custom_emoji_stickers_response_instance = GetCustomEmojiStickersResponse.from_json(json)
# print the JSON string representation of the object
print(GetCustomEmojiStickersResponse.to_json())

# convert the object into a dict
get_custom_emoji_stickers_response_dict = get_custom_emoji_stickers_response_instance.to_dict()
# create an instance of GetCustomEmojiStickersResponse from a dict
get_custom_emoji_stickers_response_from_dict = GetCustomEmojiStickersResponse.from_dict(get_custom_emoji_stickers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


