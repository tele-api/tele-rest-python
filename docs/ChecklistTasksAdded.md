# ChecklistTasksAdded

Describes a service message about tasks added to a checklist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checklist_message** | [**Message**](Message.md) |  | [optional] 
**tasks** | [**List[ChecklistTask]**](ChecklistTask.md) | List of tasks added to the checklist | 

## Example

```python
from tele_rest.models.checklist_tasks_added import ChecklistTasksAdded

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTasksAdded from a JSON string
checklist_tasks_added_instance = ChecklistTasksAdded.from_json(json)
# print the JSON string representation of the object
print(ChecklistTasksAdded.to_json())

# convert the object into a dict
checklist_tasks_added_dict = checklist_tasks_added_instance.to_dict()
# create an instance of ChecklistTasksAdded from a dict
checklist_tasks_added_from_dict = ChecklistTasksAdded.from_dict(checklist_tasks_added_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


