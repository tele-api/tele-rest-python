# PaidMessagePriceChanged

Describes a service message about a change in the price of paid messages within a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paid_message_star_count** | **int** | The new number of Telegram Stars that must be paid by non-administrator users of the supergroup chat for each sent message | 

## Example

```python
from tele_rest.models.paid_message_price_changed import PaidMessagePriceChanged

# TODO update the JSON string below
json = "{}"
# create an instance of PaidMessagePriceChanged from a JSON string
paid_message_price_changed_instance = PaidMessagePriceChanged.from_json(json)
# print the JSON string representation of the object
print(PaidMessagePriceChanged.to_json())

# convert the object into a dict
paid_message_price_changed_dict = paid_message_price_changed_instance.to_dict()
# create an instance of PaidMessagePriceChanged from a dict
paid_message_price_changed_from_dict = PaidMessagePriceChanged.from_dict(paid_message_price_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


