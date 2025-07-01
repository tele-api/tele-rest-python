# MessageOriginHiddenUser

The message was originally sent by an unknown user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the message origin, always “hidden\\_user” | [default to 'hidden_user']
**var_date** | **int** | Date the message was sent originally in Unix time | 
**sender_user_name** | **str** | Name of the user that sent the message originally | 

## Example

```python
from tele_rest.models.message_origin_hidden_user import MessageOriginHiddenUser

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOriginHiddenUser from a JSON string
message_origin_hidden_user_instance = MessageOriginHiddenUser.from_json(json)
# print the JSON string representation of the object
print(MessageOriginHiddenUser.to_json())

# convert the object into a dict
message_origin_hidden_user_dict = message_origin_hidden_user_instance.to_dict()
# create an instance of MessageOriginHiddenUser from a dict
message_origin_hidden_user_from_dict = MessageOriginHiddenUser.from_dict(message_origin_hidden_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


