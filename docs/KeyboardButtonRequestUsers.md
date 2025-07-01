# KeyboardButtonRequestUsers

This object defines the criteria used to request suitable users. Information about the selected users will be shared with the bot when the corresponding button is pressed. [More about requesting users »](https://core.telegram.org/bots/features#chat-and-user-selection)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **int** | Signed 32-bit identifier of the request that will be received back in the [UsersShared](https://core.telegram.org/bots/api/#usersshared) object. Must be unique within the message | 
**user_is_bot** | **bool** | *Optional*. Pass *True* to request bots, pass *False* to request regular users. If not specified, no additional restrictions are applied. | [optional] 
**user_is_premium** | **bool** | *Optional*. Pass *True* to request premium users, pass *False* to request non-premium users. If not specified, no additional restrictions are applied. | [optional] 
**max_quantity** | **int** | *Optional*. The maximum number of users to be selected; 1-10. Defaults to 1. | [optional] [default to 1]
**request_name** | **bool** | *Optional*. Pass *True* to request the users&#39; first and last names | [optional] 
**request_username** | **bool** | *Optional*. Pass *True* to request the users&#39; usernames | [optional] 
**request_photo** | **bool** | *Optional*. Pass *True* to request the users&#39; photos | [optional] 

## Example

```python
from tele_rest.models.keyboard_button_request_users import KeyboardButtonRequestUsers

# TODO update the JSON string below
json = "{}"
# create an instance of KeyboardButtonRequestUsers from a JSON string
keyboard_button_request_users_instance = KeyboardButtonRequestUsers.from_json(json)
# print the JSON string representation of the object
print(KeyboardButtonRequestUsers.to_json())

# convert the object into a dict
keyboard_button_request_users_dict = keyboard_button_request_users_instance.to_dict()
# create an instance of KeyboardButtonRequestUsers from a dict
keyboard_button_request_users_from_dict = KeyboardButtonRequestUsers.from_dict(keyboard_button_request_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


