# InaccessibleMessage

This object describes a message that was deleted or is otherwise inaccessible to the bot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**Chat**](Chat.md) |  | 
**message_id** | **int** | Unique message identifier inside the chat | 
**var_date** | **int** | Always 0. The field can be used to differentiate regular and inaccessible messages. | 

## Example

```python
from tele_rest.models.inaccessible_message import InaccessibleMessage

# TODO update the JSON string below
json = "{}"
# create an instance of InaccessibleMessage from a JSON string
inaccessible_message_instance = InaccessibleMessage.from_json(json)
# print the JSON string representation of the object
print(InaccessibleMessage.to_json())

# convert the object into a dict
inaccessible_message_dict = inaccessible_message_instance.to_dict()
# create an instance of InaccessibleMessage from a dict
inaccessible_message_from_dict = InaccessibleMessage.from_dict(inaccessible_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


