# ChatBoostSource

This object describes the source of a chat boost. It can be one of  * [ChatBoostSourcePremium](https://core.telegram.org/bots/api/#chatboostsourcepremium) * [ChatBoostSourceGiftCode](https://core.telegram.org/bots/api/#chatboostsourcegiftcode) * [ChatBoostSourceGiveaway](https://core.telegram.org/bots/api/#chatboostsourcegiveaway)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source of the boost, always “giveaway” | [default to 'giveaway']
**user** | [**User**](User.md) |  | 
**giveaway_message_id** | **int** | Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn&#39;t sent yet. | 
**prize_star_count** | **int** | *Optional*. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only | [optional] 
**is_unclaimed** | **bool** | *Optional*. True, if the giveaway was completed, but there was no user to win the prize | [optional] [default to True]

## Example

```python
from tele_rest.models.chat_boost_source import ChatBoostSource

# TODO update the JSON string below
json = "{}"
# create an instance of ChatBoostSource from a JSON string
chat_boost_source_instance = ChatBoostSource.from_json(json)
# print the JSON string representation of the object
print(ChatBoostSource.to_json())

# convert the object into a dict
chat_boost_source_dict = chat_boost_source_instance.to_dict()
# create an instance of ChatBoostSource from a dict
chat_boost_source_from_dict = ChatBoostSource.from_dict(chat_boost_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


