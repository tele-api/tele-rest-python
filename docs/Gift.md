# Gift

This object represents a gift that can be sent by the bot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the gift | 
**sticker** | [**Sticker**](Sticker.md) |  | 
**star_count** | **int** | The number of Telegram Stars that must be paid to send the sticker | 
**upgrade_star_count** | **int** | *Optional*. The number of Telegram Stars that must be paid to upgrade the gift to a unique one | [optional] 
**total_count** | **int** | *Optional*. The total number of the gifts of this type that can be sent; for limited gifts only | [optional] 
**remaining_count** | **int** | *Optional*. The number of remaining gifts of this type that can be sent; for limited gifts only | [optional] 
**publisher_chat** | [**Chat**](Chat.md) |  | [optional] 

## Example

```python
from tele_rest.models.gift import Gift

# TODO update the JSON string below
json = "{}"
# create an instance of Gift from a JSON string
gift_instance = Gift.from_json(json)
# print the JSON string representation of the object
print(Gift.to_json())

# convert the object into a dict
gift_dict = gift_instance.to_dict()
# create an instance of Gift from a dict
gift_from_dict = Gift.from_dict(gift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


