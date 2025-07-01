# SharedUser

This object contains information about a user that was shared with the bot using a [KeyboardButtonRequestUsers](https://core.telegram.org/bots/api/#keyboardbuttonrequestusers) button.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means. | 
**first_name** | **str** | *Optional*. First name of the user, if the name was requested by the bot | [optional] 
**last_name** | **str** | *Optional*. Last name of the user, if the name was requested by the bot | [optional] 
**username** | **str** | *Optional*. Username of the user, if the username was requested by the bot | [optional] 
**photo** | [**List[PhotoSize]**](PhotoSize.md) | *Optional*. Available sizes of the chat photo, if the photo was requested by the bot | [optional] 

## Example

```python
from tele_rest.models.shared_user import SharedUser

# TODO update the JSON string below
json = "{}"
# create an instance of SharedUser from a JSON string
shared_user_instance = SharedUser.from_json(json)
# print the JSON string representation of the object
print(SharedUser.to_json())

# convert the object into a dict
shared_user_dict = shared_user_instance.to_dict()
# create an instance of SharedUser from a dict
shared_user_from_dict = SharedUser.from_dict(shared_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


