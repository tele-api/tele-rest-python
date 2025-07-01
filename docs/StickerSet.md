# StickerSet

This object represents a sticker set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sticker set name | 
**title** | **str** | Sticker set title | 
**sticker_type** | **str** | Type of stickers in the set, currently one of “regular”, “mask”, “custom\\_emoji” | 
**stickers** | [**List[Sticker]**](Sticker.md) | List of all set stickers | 
**thumbnail** | [**PhotoSize**](PhotoSize.md) |  | [optional] 

## Example

```python
from tele_rest.models.sticker_set import StickerSet

# TODO update the JSON string below
json = "{}"
# create an instance of StickerSet from a JSON string
sticker_set_instance = StickerSet.from_json(json)
# print the JSON string representation of the object
print(StickerSet.to_json())

# convert the object into a dict
sticker_set_dict = sticker_set_instance.to_dict()
# create an instance of StickerSet from a dict
sticker_set_from_dict = StickerSet.from_dict(sticker_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


