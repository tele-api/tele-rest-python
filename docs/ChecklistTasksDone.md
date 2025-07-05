# ChecklistTasksDone

Describes a service message about checklist tasks marked as done or not done.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checklist_message** | [**Message**](Message.md) |  | [optional] 
**marked_as_done_task_ids** | **List[int]** | *Optional*. Identifiers of the tasks that were marked as done | [optional] 
**marked_as_not_done_task_ids** | **List[int]** | *Optional*. Identifiers of the tasks that were marked as not done | [optional] 

## Example

```python
from tele_rest.models.checklist_tasks_done import ChecklistTasksDone

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTasksDone from a JSON string
checklist_tasks_done_instance = ChecklistTasksDone.from_json(json)
# print the JSON string representation of the object
print(ChecklistTasksDone.to_json())

# convert the object into a dict
checklist_tasks_done_dict = checklist_tasks_done_instance.to_dict()
# create an instance of ChecklistTasksDone from a dict
checklist_tasks_done_from_dict = ChecklistTasksDone.from_dict(checklist_tasks_done_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


