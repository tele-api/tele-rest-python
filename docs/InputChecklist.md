# InputChecklist

Describes a checklist to create.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the checklist; 1-255 characters after entities parsing | 
**parse_mode** | **str** | Optional. Mode for parsing entities in the title. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**title_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the title, which can be specified instead of parse\\_mode. Currently, only *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, and *custom\\_emoji* entities are allowed. | [optional] 
**tasks** | [**List[InputChecklistTask]**](InputChecklistTask.md) | List of 1-30 tasks in the checklist | 
**others_can_add_tasks** | **bool** | *Optional*. Pass *True* if other users can add tasks to the checklist | [optional] 
**others_can_mark_tasks_as_done** | **bool** | *Optional*. Pass *True* if other users can mark tasks as done or not done in the checklist | [optional] 

## Example

```python
from tele_rest.models.input_checklist import InputChecklist

# TODO update the JSON string below
json = "{}"
# create an instance of InputChecklist from a JSON string
input_checklist_instance = InputChecklist.from_json(json)
# print the JSON string representation of the object
print(InputChecklist.to_json())

# convert the object into a dict
input_checklist_dict = input_checklist_instance.to_dict()
# create an instance of InputChecklist from a dict
input_checklist_from_dict = InputChecklist.from_dict(input_checklist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


