# ChatBoostSourcePremium

The boost was obtained by subscribing to Telegram Premium or by gifting a Telegram Premium subscription to another user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source of the boost, always “premium” | [default to 'premium']
**user** | [**User**](User.md) |  | 

## Example

```python
from tele_rest.models.chat_boost_source_premium import ChatBoostSourcePremium

# TODO update the JSON string below
json = "{}"
# create an instance of ChatBoostSourcePremium from a JSON string
chat_boost_source_premium_instance = ChatBoostSourcePremium.from_json(json)
# print the JSON string representation of the object
print(ChatBoostSourcePremium.to_json())

# convert the object into a dict
chat_boost_source_premium_dict = chat_boost_source_premium_instance.to_dict()
# create an instance of ChatBoostSourcePremium from a dict
chat_boost_source_premium_from_dict = ChatBoostSourcePremium.from_dict(chat_boost_source_premium_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


