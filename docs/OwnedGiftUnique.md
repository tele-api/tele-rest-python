# OwnedGiftUnique

Describes a unique gift received and owned by a user or a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the gift, always “unique” | [default to 'unique']
**gift** | [**UniqueGift**](UniqueGift.md) |  | 
**owned_gift_id** | **str** | *Optional*. Unique identifier of the received gift for the bot; for gifts received on behalf of business accounts only | [optional] 
**sender_user** | [**User**](User.md) |  | [optional] 
**send_date** | **int** | Date the gift was sent in Unix time | 
**is_saved** | **bool** | *Optional*. True, if the gift is displayed on the account&#39;s profile page; for gifts received on behalf of business accounts only | [optional] [default to True]
**can_be_transferred** | **bool** | *Optional*. True, if the gift can be transferred to another owner; for gifts received on behalf of business accounts only | [optional] [default to True]
**transfer_star_count** | **int** | *Optional*. Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift | [optional] 

## Example

```python
from tele_rest.models.owned_gift_unique import OwnedGiftUnique

# TODO update the JSON string below
json = "{}"
# create an instance of OwnedGiftUnique from a JSON string
owned_gift_unique_instance = OwnedGiftUnique.from_json(json)
# print the JSON string representation of the object
print(OwnedGiftUnique.to_json())

# convert the object into a dict
owned_gift_unique_dict = owned_gift_unique_instance.to_dict()
# create an instance of OwnedGiftUnique from a dict
owned_gift_unique_from_dict = OwnedGiftUnique.from_dict(owned_gift_unique_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


