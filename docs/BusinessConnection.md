# BusinessConnection

Describes the connection of the bot with a business account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the business connection | 
**user** | [**User**](User.md) |  | 
**user_chat_id** | **int** | Identifier of a private chat with the user who created the business connection. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. | 
**var_date** | **int** | Date the connection was established in Unix time | 
**rights** | [**BusinessBotRights**](BusinessBotRights.md) |  | [optional] 
**is_enabled** | **bool** | *True*, if the connection is active | 

## Example

```python
from tele_rest.models.business_connection import BusinessConnection

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessConnection from a JSON string
business_connection_instance = BusinessConnection.from_json(json)
# print the JSON string representation of the object
print(BusinessConnection.to_json())

# convert the object into a dict
business_connection_dict = business_connection_instance.to_dict()
# create an instance of BusinessConnection from a dict
business_connection_from_dict = BusinessConnection.from_dict(business_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


