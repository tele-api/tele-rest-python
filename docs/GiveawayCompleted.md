# GiveawayCompleted

This object represents a service message about the completion of a giveaway without public winners.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**winner_count** | **int** | Number of winners in the giveaway | 
**unclaimed_prize_count** | **int** | *Optional*. Number of undistributed prizes | [optional] 
**giveaway_message** | [**Message**](Message.md) |  | [optional] 
**is_star_giveaway** | **bool** | *Optional*. *True*, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway. | [optional] [default to True]

## Example

```python
from tele_rest.models.giveaway_completed import GiveawayCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of GiveawayCompleted from a JSON string
giveaway_completed_instance = GiveawayCompleted.from_json(json)
# print the JSON string representation of the object
print(GiveawayCompleted.to_json())

# convert the object into a dict
giveaway_completed_dict = giveaway_completed_instance.to_dict()
# create an instance of GiveawayCompleted from a dict
giveaway_completed_from_dict = GiveawayCompleted.from_dict(giveaway_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


