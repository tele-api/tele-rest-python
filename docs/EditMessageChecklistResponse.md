# EditMessageChecklistResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.edit_message_checklist_response import EditMessageChecklistResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageChecklistResponse from a JSON string
edit_message_checklist_response_instance = EditMessageChecklistResponse.from_json(json)
# print the JSON string representation of the object
print(EditMessageChecklistResponse.to_json())

# convert the object into a dict
edit_message_checklist_response_dict = edit_message_checklist_response_instance.to_dict()
# create an instance of EditMessageChecklistResponse from a dict
edit_message_checklist_response_from_dict = EditMessageChecklistResponse.from_dict(edit_message_checklist_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


