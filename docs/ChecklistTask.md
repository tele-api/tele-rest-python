# ChecklistTask

Describes a task in a checklist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the task | 
**text** | **str** | Text of the task | 
**text_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. Special entities that appear in the task text | [optional] 
**completed_by_user** | [**User**](User.md) |  | [optional] 
**completed_by_chat** | [**Chat**](Chat.md) |  | [optional] 
**completion_date** | **int** | *Optional*. Point in time (Unix timestamp) when the task was completed; 0 if the task wasn&#39;t completed | [optional] 

## Example

```python
from tele_rest.models.checklist_task import ChecklistTask

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTask from a JSON string
checklist_task_instance = ChecklistTask.from_json(json)
# print the JSON string representation of the object
print(ChecklistTask.to_json())

# convert the object into a dict
checklist_task_dict = checklist_task_instance.to_dict()
# create an instance of ChecklistTask from a dict
checklist_task_from_dict = ChecklistTask.from_dict(checklist_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


