# UniqueGiftModel

This object describes the model of a unique gift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the model | 
**sticker** | [**Sticker**](Sticker.md) |  | 
**rarity_per_mille** | **int** | The number of unique gifts that receive this model for every 1000 gifts upgraded | 

## Example

```python
from tele_rest.models.unique_gift_model import UniqueGiftModel

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueGiftModel from a JSON string
unique_gift_model_instance = UniqueGiftModel.from_json(json)
# print the JSON string representation of the object
print(UniqueGiftModel.to_json())

# convert the object into a dict
unique_gift_model_dict = unique_gift_model_instance.to_dict()
# create an instance of UniqueGiftModel from a dict
unique_gift_model_from_dict = UniqueGiftModel.from_dict(unique_gift_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


