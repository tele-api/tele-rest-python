# MessageOriginUser

The message was originally sent by a known user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the message origin, always “user” | [default to 'user']
**var_date** | **int** | Date the message was sent originally in Unix time | 
**sender_user** | [**User**](User.md) |  | 

## Example

```python
from tele_rest.models.message_origin_user import MessageOriginUser

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOriginUser from a JSON string
message_origin_user_instance = MessageOriginUser.from_json(json)
# print the JSON string representation of the object
print(MessageOriginUser.to_json())

# convert the object into a dict
message_origin_user_dict = message_origin_user_instance.to_dict()
# create an instance of MessageOriginUser from a dict
message_origin_user_from_dict = MessageOriginUser.from_dict(message_origin_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


