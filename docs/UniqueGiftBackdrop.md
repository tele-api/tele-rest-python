# UniqueGiftBackdrop

This object describes the backdrop of a unique gift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the backdrop | 
**colors** | [**UniqueGiftBackdropColors**](UniqueGiftBackdropColors.md) |  | 
**rarity_per_mille** | **int** | The number of unique gifts that receive this backdrop for every 1000 gifts upgraded | 

## Example

```python
from tele_rest.models.unique_gift_backdrop import UniqueGiftBackdrop

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueGiftBackdrop from a JSON string
unique_gift_backdrop_instance = UniqueGiftBackdrop.from_json(json)
# print the JSON string representation of the object
print(UniqueGiftBackdrop.to_json())

# convert the object into a dict
unique_gift_backdrop_dict = unique_gift_backdrop_instance.to_dict()
# create an instance of UniqueGiftBackdrop from a dict
unique_gift_backdrop_from_dict = UniqueGiftBackdrop.from_dict(unique_gift_backdrop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


