# UniqueGiftInfo

Describes a service message about a unique gift that was sent or received.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift** | [**UniqueGift**](UniqueGift.md) |  | 
**origin** | **str** | Origin of the gift. Currently, either “upgrade” for gifts upgraded from regular gifts, “transfer” for gifts transferred from other users or channels, “resale” for gifts bought from other users, “gifted\\_upgrade” for upgrades purchased after the gift was sent, or “offer” for gifts bought or sold through gift purchase offers | 
**last_resale_currency** | **str** | *Optional*. For gifts bought from other users, the currency in which the payment for the gift was done. Currently, one of “XTR” for Telegram Stars or “TON” for toncoins. | [optional] 
**last_resale_amount** | **int** | *Optional*. For gifts bought from other users, the price paid for the gift in either Telegram Stars or nanotoncoins | [optional] 
**owned_gift_id** | **str** | *Optional*. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts | [optional] 
**transfer_star_count** | **int** | *Optional*. Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift | [optional] 
**next_transfer_date** | **int** | *Optional*. Point in time (Unix timestamp) when the gift can be transferred. If it is in the past, then the gift can be transferred now | [optional] 

## Example

```python
from tele_rest.models.unique_gift_info import UniqueGiftInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueGiftInfo from a JSON string
unique_gift_info_instance = UniqueGiftInfo.from_json(json)
# print the JSON string representation of the object
print(UniqueGiftInfo.to_json())

# convert the object into a dict
unique_gift_info_dict = unique_gift_info_instance.to_dict()
# create an instance of UniqueGiftInfo from a dict
unique_gift_info_from_dict = UniqueGiftInfo.from_dict(unique_gift_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


