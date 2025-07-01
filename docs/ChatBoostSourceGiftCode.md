# ChatBoostSourceGiftCode

The boost was obtained by the creation of Telegram Premium gift codes to boost a chat. Each such code boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source of the boost, always “gift\\_code” | [default to 'gift_code']
**user** | [**User**](User.md) |  | 

## Example

```python
from tele_rest.models.chat_boost_source_gift_code import ChatBoostSourceGiftCode

# TODO update the JSON string below
json = "{}"
# create an instance of ChatBoostSourceGiftCode from a JSON string
chat_boost_source_gift_code_instance = ChatBoostSourceGiftCode.from_json(json)
# print the JSON string representation of the object
print(ChatBoostSourceGiftCode.to_json())

# convert the object into a dict
chat_boost_source_gift_code_dict = chat_boost_source_gift_code_instance.to_dict()
# create an instance of ChatBoostSourceGiftCode from a dict
chat_boost_source_gift_code_from_dict = ChatBoostSourceGiftCode.from_dict(chat_boost_source_gift_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


