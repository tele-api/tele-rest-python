# Sticker

This object represents a sticker.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | Identifier for this file, which can be used to download or reuse the file | 
**file_unique_id** | **str** | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can&#39;t be used to download or reuse the file. | 
**type** | **str** | Type of the sticker, currently one of “regular”, “mask”, “custom\\_emoji”. The type of the sticker is independent from its format, which is determined by the fields *is\\_animated* and *is\\_video*. | 
**width** | **int** | Sticker width | 
**height** | **int** | Sticker height | 
**is_animated** | **bool** | *True*, if the sticker is [animated](https://telegram.org/blog/animated-stickers) | 
**is_video** | **bool** | *True*, if the sticker is a [video sticker](https://telegram.org/blog/video-stickers-better-reactions) | 
**thumbnail** | [**PhotoSize**](PhotoSize.md) |  | [optional] 
**emoji** | **str** | *Optional*. Emoji associated with the sticker | [optional] 
**set_name** | **str** | *Optional*. Name of the sticker set to which the sticker belongs | [optional] 
**premium_animation** | [**File**](File.md) |  | [optional] 
**mask_position** | [**MaskPosition**](MaskPosition.md) |  | [optional] 
**custom_emoji_id** | **str** | *Optional*. For custom emoji stickers, unique identifier of the custom emoji | [optional] 
**needs_repainting** | **bool** | *Optional*. *True*, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places | [optional] [default to True]
**file_size** | **int** | *Optional*. File size in bytes | [optional] 

## Example

```python
from tele_rest.models.sticker import Sticker

# TODO update the JSON string below
json = "{}"
# create an instance of Sticker from a JSON string
sticker_instance = Sticker.from_json(json)
# print the JSON string representation of the object
print(Sticker.to_json())

# convert the object into a dict
sticker_dict = sticker_instance.to_dict()
# create an instance of Sticker from a dict
sticker_from_dict = Sticker.from_dict(sticker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


