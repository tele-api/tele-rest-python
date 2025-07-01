# UniqueGiftSymbol

This object describes the symbol shown on the pattern of a unique gift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the symbol | 
**sticker** | [**Sticker**](Sticker.md) |  | 
**rarity_per_mille** | **int** | The number of unique gifts that receive this model for every 1000 gifts upgraded | 

## Example

```python
from tele_rest.models.unique_gift_symbol import UniqueGiftSymbol

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueGiftSymbol from a JSON string
unique_gift_symbol_instance = UniqueGiftSymbol.from_json(json)
# print the JSON string representation of the object
print(UniqueGiftSymbol.to_json())

# convert the object into a dict
unique_gift_symbol_dict = unique_gift_symbol_instance.to_dict()
# create an instance of UniqueGiftSymbol from a dict
unique_gift_symbol_from_dict = UniqueGiftSymbol.from_dict(unique_gift_symbol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


