# GiveawayWinners

This object represents a message about the completion of a giveaway with public winners.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**Chat**](Chat.md) |  | 
**giveaway_message_id** | **int** | Identifier of the message with the giveaway in the chat | 
**winners_selection_date** | **int** | Point in time (Unix timestamp) when winners of the giveaway were selected | 
**winner_count** | **int** | Total number of winners in the giveaway | 
**winners** | [**List[User]**](User.md) | List of up to 100 winners of the giveaway | 
**additional_chat_count** | **int** | *Optional*. The number of other chats the user had to join in order to be eligible for the giveaway | [optional] 
**prize_star_count** | **int** | *Optional*. The number of Telegram Stars that were split between giveaway winners; for Telegram Star giveaways only | [optional] 
**premium_subscription_month_count** | **int** | *Optional*. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only | [optional] 
**unclaimed_prize_count** | **int** | *Optional*. Number of undistributed prizes | [optional] 
**only_new_members** | **bool** | *Optional*. *True*, if only users who had joined the chats after the giveaway started were eligible to win | [optional] [default to True]
**was_refunded** | **bool** | *Optional*. *True*, if the giveaway was canceled because the payment for it was refunded | [optional] [default to True]
**prize_description** | **str** | *Optional*. Description of additional giveaway prize | [optional] 

## Example

```python
from tele_rest.models.giveaway_winners import GiveawayWinners

# TODO update the JSON string below
json = "{}"
# create an instance of GiveawayWinners from a JSON string
giveaway_winners_instance = GiveawayWinners.from_json(json)
# print the JSON string representation of the object
print(GiveawayWinners.to_json())

# convert the object into a dict
giveaway_winners_dict = giveaway_winners_instance.to_dict()
# create an instance of GiveawayWinners from a dict
giveaway_winners_from_dict = GiveawayWinners.from_dict(giveaway_winners_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


