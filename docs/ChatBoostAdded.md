# ChatBoostAdded

This object represents a service message about a user boosting a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boost_count** | **int** | Number of boosts added by the user | 

## Example

```python
from tele_rest.models.chat_boost_added import ChatBoostAdded

# TODO update the JSON string below
json = "{}"
# create an instance of ChatBoostAdded from a JSON string
chat_boost_added_instance = ChatBoostAdded.from_json(json)
# print the JSON string representation of the object
print(ChatBoostAdded.to_json())

# convert the object into a dict
chat_boost_added_dict = chat_boost_added_instance.to_dict()
# create an instance of ChatBoostAdded from a dict
chat_boost_added_from_dict = ChatBoostAdded.from_dict(chat_boost_added_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


