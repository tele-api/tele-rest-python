# Dice

This object represents an animated emoji that displays a random value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emoji** | **str** | Emoji on which the dice throw animation is based | 
**value** | **int** | Value of the dice, 1-6 for “🎲”, “🎯” and “🎳” base emoji, 1-5 for “🏀” and “⚽” base emoji, 1-64 for “🎰” base emoji | 

## Example

```python
from tele_rest.models.dice import Dice

# TODO update the JSON string below
json = "{}"
# create an instance of Dice from a JSON string
dice_instance = Dice.from_json(json)
# print the JSON string representation of the object
print(Dice.to_json())

# convert the object into a dict
dice_dict = dice_instance.to_dict()
# create an instance of Dice from a dict
dice_from_dict = Dice.from_dict(dice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


