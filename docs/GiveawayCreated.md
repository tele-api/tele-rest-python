# GiveawayCreated

This object represents a service message about the creation of a scheduled giveaway.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prize_star_count** | **int** | *Optional*. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only | [optional] 

## Example

```python
from tele_rest.models.giveaway_created import GiveawayCreated

# TODO update the JSON string below
json = "{}"
# create an instance of GiveawayCreated from a JSON string
giveaway_created_instance = GiveawayCreated.from_json(json)
# print the JSON string representation of the object
print(GiveawayCreated.to_json())

# convert the object into a dict
giveaway_created_dict = giveaway_created_instance.to_dict()
# create an instance of GiveawayCreated from a dict
giveaway_created_from_dict = GiveawayCreated.from_dict(giveaway_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


