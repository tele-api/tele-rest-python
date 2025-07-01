# ChatBoost

This object contains information about a chat boost.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boost_id** | **str** | Unique identifier of the boost | 
**add_date** | **int** | Point in time (Unix timestamp) when the chat was boosted | 
**expiration_date** | **int** | Point in time (Unix timestamp) when the boost will automatically expire, unless the booster&#39;s Telegram Premium subscription is prolonged | 
**source** | [**ChatBoostSource**](ChatBoostSource.md) |  | 

## Example

```python
from tele_rest.models.chat_boost import ChatBoost

# TODO update the JSON string below
json = "{}"
# create an instance of ChatBoost from a JSON string
chat_boost_instance = ChatBoost.from_json(json)
# print the JSON string representation of the object
print(ChatBoost.to_json())

# convert the object into a dict
chat_boost_dict = chat_boost_instance.to_dict()
# create an instance of ChatBoost from a dict
chat_boost_from_dict = ChatBoost.from_dict(chat_boost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


