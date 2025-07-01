# BotName

This object represents the bot's name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The bot&#39;s name | 

## Example

```python
from tele_rest.models.bot_name import BotName

# TODO update the JSON string below
json = "{}"
# create an instance of BotName from a JSON string
bot_name_instance = BotName.from_json(json)
# print the JSON string representation of the object
print(BotName.to_json())

# convert the object into a dict
bot_name_dict = bot_name_instance.to_dict()
# create an instance of BotName from a dict
bot_name_from_dict = BotName.from_dict(bot_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


