# Giveaway

This object represents a message about a scheduled giveaway.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chats** | [**List[Chat]**](Chat.md) | The list of chats which the user must join to participate in the giveaway | 
**winners_selection_date** | **int** | Point in time (Unix timestamp) when winners of the giveaway will be selected | 
**winner_count** | **int** | The number of users which are supposed to be selected as winners of the giveaway | 
**only_new_members** | **bool** | *Optional*. *True*, if only users who join the chats after the giveaway started should be eligible to win | [optional] [default to True]
**has_public_winners** | **bool** | *Optional*. *True*, if the list of giveaway winners will be visible to everyone | [optional] [default to True]
**prize_description** | **str** | *Optional*. Description of additional giveaway prize | [optional] 
**country_codes** | **List[str]** | *Optional*. A list of two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway. Users with a phone number that was bought on Fragment can always participate in giveaways. | [optional] 
**prize_star_count** | **int** | *Optional*. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only | [optional] 
**premium_subscription_month_count** | **int** | *Optional*. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only | [optional] 

## Example

```python
from tele_rest.models.giveaway import Giveaway

# TODO update the JSON string below
json = "{}"
# create an instance of Giveaway from a JSON string
giveaway_instance = Giveaway.from_json(json)
# print the JSON string representation of the object
print(Giveaway.to_json())

# convert the object into a dict
giveaway_dict = giveaway_instance.to_dict()
# create an instance of Giveaway from a dict
giveaway_from_dict = Giveaway.from_dict(giveaway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


