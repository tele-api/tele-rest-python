# UserChatBoosts

This object represents a list of boosts added to a chat by a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boosts** | [**List[ChatBoost]**](ChatBoost.md) | The list of boosts added to the chat by the user | 

## Example

```python
from tele_rest.models.user_chat_boosts import UserChatBoosts

# TODO update the JSON string below
json = "{}"
# create an instance of UserChatBoosts from a JSON string
user_chat_boosts_instance = UserChatBoosts.from_json(json)
# print the JSON string representation of the object
print(UserChatBoosts.to_json())

# convert the object into a dict
user_chat_boosts_dict = user_chat_boosts_instance.to_dict()
# create an instance of UserChatBoosts from a dict
user_chat_boosts_from_dict = UserChatBoosts.from_dict(user_chat_boosts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


