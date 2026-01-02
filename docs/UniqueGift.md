# UniqueGift

This object describes a unique gift that was upgraded from a regular gift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_id** | **str** | Identifier of the regular gift from which the gift was upgraded | 
**base_name** | **str** | Human-readable name of the regular gift from which this unique gift was upgraded | 
**name** | **str** | Unique name of the gift. This name can be used in &#x60;https://t.me/nft/...&#x60; links and story areas | 
**number** | **int** | Unique number of the upgraded gift among gifts upgraded from the same regular gift | 
**model** | [**UniqueGiftModel**](UniqueGiftModel.md) |  | 
**symbol** | [**UniqueGiftSymbol**](UniqueGiftSymbol.md) |  | 
**backdrop** | [**UniqueGiftBackdrop**](UniqueGiftBackdrop.md) |  | 
**is_premium** | **bool** | *Optional*. *True*, if the original regular gift was exclusively purchaseable by Telegram Premium subscribers | [optional] [default to True]
**is_from_blockchain** | **bool** | *Optional*. *True*, if the gift is assigned from the TON blockchain and can&#39;t be resold or transferred in Telegram | [optional] [default to True]
**colors** | [**UniqueGiftColors**](UniqueGiftColors.md) |  | [optional] 
**publisher_chat** | [**Chat**](Chat.md) |  | [optional] 

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


