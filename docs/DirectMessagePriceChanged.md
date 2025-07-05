# DirectMessagePriceChanged

Describes a service message about a change in the price of direct messages sent to a channel chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**are_direct_messages_enabled** | **bool** | *True*, if direct messages are enabled for the channel chat; false otherwise | 
**direct_message_star_count** | **int** | *Optional*. The new number of Telegram Stars that must be paid by users for each direct message sent to the channel. Does not apply to users who have been exempted by administrators. Defaults to 0. | [optional] [default to 0]

## Example

```python
from tele_rest.models.direct_message_price_changed import DirectMessagePriceChanged

# TODO update the JSON string below
json = "{}"
# create an instance of DirectMessagePriceChanged from a JSON string
direct_message_price_changed_instance = DirectMessagePriceChanged.from_json(json)
# print the JSON string representation of the object
print(DirectMessagePriceChanged.to_json())

# convert the object into a dict
direct_message_price_changed_dict = direct_message_price_changed_instance.to_dict()
# create an instance of DirectMessagePriceChanged from a dict
direct_message_price_changed_from_dict = DirectMessagePriceChanged.from_dict(direct_message_price_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


