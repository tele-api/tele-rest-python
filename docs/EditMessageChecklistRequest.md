# EditMessageChecklistRequest

Request parameters for editMessageChecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be sent | 
**chat_id** | **int** | Unique identifier for the target chat | 
**message_id** | **int** | Unique identifier for the target message | 
**checklist** | [**InputChecklist**](InputChecklist.md) |  | 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.edit_message_checklist_request import EditMessageChecklistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageChecklistRequest from a JSON string
edit_message_checklist_request_instance = EditMessageChecklistRequest.from_json(json)
# print the JSON string representation of the object
print(EditMessageChecklistRequest.to_json())

# convert the object into a dict
edit_message_checklist_request_dict = edit_message_checklist_request_instance.to_dict()
# create an instance of EditMessageChecklistRequest from a dict
edit_message_checklist_request_from_dict = EditMessageChecklistRequest.from_dict(edit_message_checklist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


