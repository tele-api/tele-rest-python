# UsersShared

This object contains information about the users whose identifiers were shared with the bot using a [KeyboardButtonRequestUsers](https://core.telegram.org/bots/api/#keyboardbuttonrequestusers) button.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **int** | Identifier of the request | 
**users** | [**List[SharedUser]**](SharedUser.md) | Information about users shared with the bot. | 

## Example

```python
from tele_rest.models.users_shared import UsersShared

# TODO update the JSON string below
json = "{}"
# create an instance of UsersShared from a JSON string
users_shared_instance = UsersShared.from_json(json)
# print the JSON string representation of the object
print(UsersShared.to_json())

# convert the object into a dict
users_shared_dict = users_shared_instance.to_dict()
# create an instance of UsersShared from a dict
users_shared_from_dict = UsersShared.from_dict(users_shared_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


