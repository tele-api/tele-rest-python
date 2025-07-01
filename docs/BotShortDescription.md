# BotShortDescription

This object represents the bot's short description.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_description** | **str** | The bot&#39;s short description | 

## Example

```python
from tele_rest.models.bot_short_description import BotShortDescription

# TODO update the JSON string below
json = "{}"
# create an instance of BotShortDescription from a JSON string
bot_short_description_instance = BotShortDescription.from_json(json)
# print the JSON string representation of the object
print(BotShortDescription.to_json())

# convert the object into a dict
bot_short_description_dict = bot_short_description_instance.to_dict()
# create an instance of BotShortDescription from a dict
bot_short_description_from_dict = BotShortDescription.from_dict(bot_short_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


