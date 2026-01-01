# OwnedGiftRegular

Describes a regular gift owned by a user or a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the gift, always “regular” | [default to 'regular']
**gift** | [**Gift**](Gift.md) |  | 
**owned_gift_id** | **str** | *Optional*. Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only | [optional] 
**sender_user** | [**User**](User.md) |  | [optional] 
**send_date** | **int** | Date the gift was sent in Unix time | 
**text** | **str** | *Optional*. Text of the message that was added to the gift | [optional] 
**entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. Special entities that appear in the text | [optional] 
**is_private** | **bool** | *Optional*. *True*, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them | [optional] [default to True]
**is_saved** | **bool** | *Optional*. *True*, if the gift is displayed on the account&#39;s profile page; for gifts received on behalf of business accounts only | [optional] [default to True]
**can_be_upgraded** | **bool** | *Optional*. *True*, if the gift can be upgraded to a unique gift; for gifts received on behalf of business accounts only | [optional] [default to True]
**was_refunded** | **bool** | *Optional*. *True*, if the gift was refunded and isn&#39;t available anymore | [optional] [default to True]
**convert_star_count** | **int** | *Optional*. Number of Telegram Stars that can be claimed by the receiver instead of the gift; omitted if the gift cannot be converted to Telegram Stars; for gifts received on behalf of business accounts only | [optional] 
**prepaid_upgrade_star_count** | **int** | *Optional*. Number of Telegram Stars that were paid for the ability to upgrade the gift | [optional] 
**is_upgrade_separate** | **bool** | *Optional*. *True*, if the gift&#39;s upgrade was purchased after the gift was sent; for gifts received on behalf of business accounts only | [optional] [default to True]
**unique_gift_number** | **int** | *Optional*. Unique number reserved for this gift when upgraded. See the *number* field in [UniqueGift](https://core.telegram.org/bots/api/#uniquegift) | [optional] 

## Example

```python
from tele_rest.models.owned_gift_regular import OwnedGiftRegular

# TODO update the JSON string below
json = "{}"
# create an instance of OwnedGiftRegular from a JSON string
owned_gift_regular_instance = OwnedGiftRegular.from_json(json)
# print the JSON string representation of the object
print(OwnedGiftRegular.to_json())

# convert the object into a dict
owned_gift_regular_dict = owned_gift_regular_instance.to_dict()
# create an instance of OwnedGiftRegular from a dict
owned_gift_regular_from_dict = OwnedGiftRegular.from_dict(owned_gift_regular_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


