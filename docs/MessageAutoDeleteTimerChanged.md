# MessageAutoDeleteTimerChanged

This object represents a service message about a change in auto-delete timer settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_auto_delete_time** | **int** | New auto-delete time for messages in the chat; in seconds | 

## Example

```python
from tele_rest.models.message_auto_delete_timer_changed import MessageAutoDeleteTimerChanged

# TODO update the JSON string below
json = "{}"
# create an instance of MessageAutoDeleteTimerChanged from a JSON string
message_auto_delete_timer_changed_instance = MessageAutoDeleteTimerChanged.from_json(json)
# print the JSON string representation of the object
print(MessageAutoDeleteTimerChanged.to_json())

# convert the object into a dict
message_auto_delete_timer_changed_dict = message_auto_delete_timer_changed_instance.to_dict()
# create an instance of MessageAutoDeleteTimerChanged from a dict
message_auto_delete_timer_changed_from_dict = MessageAutoDeleteTimerChanged.from_dict(message_auto_delete_timer_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


