# ChatBoostSourceGiveaway

The boost was obtained by the creation of a Telegram Premium or a Telegram Star giveaway. This boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription for Telegram Premium giveaways and *prize\\_star\\_count* / 500 times for one year for Telegram Star giveaways.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source of the boost, always “giveaway” | [default to 'giveaway']
**giveaway_message_id** | **int** | Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn&#39;t sent yet. | 
**user** | [**User**](User.md) |  | [optional] 
**prize_star_count** | **int** | *Optional*. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only | [optional] 
**is_unclaimed** | **bool** | *Optional*. *True*, if the giveaway was completed, but there was no user to win the prize | [optional] [default to True]

## Example

```python
from tele_rest.models.chat_boost_source_giveaway import ChatBoostSourceGiveaway

# TODO update the JSON string below
json = "{}"
# create an instance of ChatBoostSourceGiveaway from a JSON string
chat_boost_source_giveaway_instance = ChatBoostSourceGiveaway.from_json(json)
# print the JSON string representation of the object
print(ChatBoostSourceGiveaway.to_json())

# convert the object into a dict
chat_boost_source_giveaway_dict = chat_boost_source_giveaway_instance.to_dict()
# create an instance of ChatBoostSourceGiveaway from a dict
chat_boost_source_giveaway_from_dict = ChatBoostSourceGiveaway.from_dict(chat_boost_source_giveaway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


