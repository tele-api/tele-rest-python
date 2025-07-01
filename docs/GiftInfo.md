# GiftInfo

Describes a service message about a regular gift that was sent or received.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift** | [**Gift**](Gift.md) |  | 
**owned_gift_id** | **str** | *Optional*. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts | [optional] 
**convert_star_count** | **int** | *Optional*. Number of Telegram Stars that can be claimed by the receiver by converting the gift; omitted if conversion to Telegram Stars is impossible | [optional] 
**prepaid_upgrade_star_count** | **int** | *Optional*. Number of Telegram Stars that were prepaid by the sender for the ability to upgrade the gift | [optional] 
**can_be_upgraded** | **bool** | *Optional*. True, if the gift can be upgraded to a unique gift | [optional] [default to True]
**text** | **str** | *Optional*. Text of the message that was added to the gift | [optional] 
**entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. Special entities that appear in the text | [optional] 
**is_private** | **bool** | *Optional*. True, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them | [optional] [default to True]

## Example

```python
from tele_rest.models.gift_info import GiftInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GiftInfo from a JSON string
gift_info_instance = GiftInfo.from_json(json)
# print the JSON string representation of the object
print(GiftInfo.to_json())

# convert the object into a dict
gift_info_dict = gift_info_instance.to_dict()
# create an instance of GiftInfo from a dict
gift_info_from_dict = GiftInfo.from_dict(gift_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


