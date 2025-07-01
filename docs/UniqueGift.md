# UniqueGift

This object describes a unique gift that was upgraded from a regular gift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_name** | **str** | Human-readable name of the regular gift from which this unique gift was upgraded | 
**name** | **str** | Unique name of the gift. This name can be used in &#x60;https://t.me/nft/...&#x60; links and story areas | 
**number** | **int** | Unique number of the upgraded gift among gifts upgraded from the same regular gift | 
**model** | [**UniqueGiftModel**](UniqueGiftModel.md) |  | 
**symbol** | [**UniqueGiftSymbol**](UniqueGiftSymbol.md) |  | 
**backdrop** | [**UniqueGiftBackdrop**](UniqueGiftBackdrop.md) |  | 

## Example

```python
from tele_rest.models.unique_gift import UniqueGift

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueGift from a JSON string
unique_gift_instance = UniqueGift.from_json(json)
# print the JSON string representation of the object
print(UniqueGift.to_json())

# convert the object into a dict
unique_gift_dict = unique_gift_instance.to_dict()
# create an instance of UniqueGift from a dict
unique_gift_from_dict = UniqueGift.from_dict(unique_gift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


