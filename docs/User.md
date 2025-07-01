# User

This object represents a Telegram user or bot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. | 
**is_bot** | **bool** | *True*, if this user is a bot | 
**first_name** | **str** | User&#39;s or bot&#39;s first name | 
**last_name** | **str** | *Optional*. User&#39;s or bot&#39;s last name | [optional] 
**username** | **str** | *Optional*. User&#39;s or bot&#39;s username | [optional] 
**language_code** | **str** | *Optional*. [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) of the user&#39;s language | [optional] 
**is_premium** | **bool** | *Optional*. *True*, if this user is a Telegram Premium user | [optional] [default to True]
**added_to_attachment_menu** | **bool** | *Optional*. *True*, if this user added the bot to the attachment menu | [optional] [default to True]
**can_join_groups** | **bool** | *Optional*. *True*, if the bot can be invited to groups. Returned only in [getMe](https://core.telegram.org/bots/api/#getme). | [optional] 
**can_read_all_group_messages** | **bool** | *Optional*. *True*, if [privacy mode](https://core.telegram.org/bots/features#privacy-mode) is disabled for the bot. Returned only in [getMe](https://core.telegram.org/bots/api/#getme). | [optional] 
**supports_inline_queries** | **bool** | *Optional*. *True*, if the bot supports inline queries. Returned only in [getMe](https://core.telegram.org/bots/api/#getme). | [optional] 
**can_connect_to_business** | **bool** | *Optional*. *True*, if the bot can be connected to a Telegram Business account to receive its messages. Returned only in [getMe](https://core.telegram.org/bots/api/#getme). | [optional] 
**has_main_web_app** | **bool** | *Optional*. *True*, if the bot has a main Web App. Returned only in [getMe](https://core.telegram.org/bots/api/#getme). | [optional] 

## Example

```python
from tele_rest.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


