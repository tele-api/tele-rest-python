# AcceptedGiftTypes

This object describes the types of gifts that can be gifted to a user or a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unlimited_gifts** | **bool** | *True*, if unlimited regular gifts are accepted | 
**limited_gifts** | **bool** | *True*, if limited regular gifts are accepted | 
**unique_gifts** | **bool** | *True*, if unique gifts or gifts that can be upgraded to unique for free are accepted | 
**premium_subscription** | **bool** | *True*, if a Telegram Premium subscription is accepted | 

## Example

```python
from tele_rest.models.accepted_gift_types import AcceptedGiftTypes

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedGiftTypes from a JSON string
accepted_gift_types_instance = AcceptedGiftTypes.from_json(json)
# print the JSON string representation of the object
print(AcceptedGiftTypes.to_json())

# convert the object into a dict
accepted_gift_types_dict = accepted_gift_types_instance.to_dict()
# create an instance of AcceptedGiftTypes from a dict
accepted_gift_types_from_dict = AcceptedGiftTypes.from_dict(accepted_gift_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


