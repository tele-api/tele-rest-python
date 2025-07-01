# ChatBoostRemoved

This object represents a boost removed from a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**Chat**](Chat.md) |  | 
**boost_id** | **str** | Unique identifier of the boost | 
**remove_date** | **int** | Point in time (Unix timestamp) when the boost was removed | 
**source** | [**ChatBoostSource**](ChatBoostSource.md) |  | 

## Example

```python
from tele_rest.models.chat_boost_removed import ChatBoostRemoved

# TODO update the JSON string below
json = "{}"
# create an instance of ChatBoostRemoved from a JSON string
chat_boost_removed_instance = ChatBoostRemoved.from_json(json)
# print the JSON string representation of the object
print(ChatBoostRemoved.to_json())

# convert the object into a dict
chat_boost_removed_dict = chat_boost_removed_instance.to_dict()
# create an instance of ChatBoostRemoved from a dict
chat_boost_removed_from_dict = ChatBoostRemoved.from_dict(chat_boost_removed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


