# BotDescription

This object represents the bot's description.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The bot&#39;s description | 

## Example

```python
from tele_rest.models.bot_description import BotDescription

# TODO update the JSON string below
json = "{}"
# create an instance of BotDescription from a JSON string
bot_description_instance = BotDescription.from_json(json)
# print the JSON string representation of the object
print(BotDescription.to_json())

# convert the object into a dict
bot_description_dict = bot_description_instance.to_dict()
# create an instance of BotDescription from a dict
bot_description_from_dict = BotDescription.from_dict(bot_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


