# ChatBoostUpdated

This object represents a boost added to a chat or changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**Chat**](Chat.md) |  | 
**boost** | [**ChatBoost**](ChatBoost.md) |  | 

## Example

```python
from tele_rest.models.chat_boost_updated import ChatBoostUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of ChatBoostUpdated from a JSON string
chat_boost_updated_instance = ChatBoostUpdated.from_json(json)
# print the JSON string representation of the object
print(ChatBoostUpdated.to_json())

# convert the object into a dict
chat_boost_updated_dict = chat_boost_updated_instance.to_dict()
# create an instance of ChatBoostUpdated from a dict
chat_boost_updated_from_dict = ChatBoostUpdated.from_dict(chat_boost_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


