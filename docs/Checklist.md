# Checklist

Describes a checklist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the checklist | 
**title_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. Special entities that appear in the checklist title | [optional] 
**tasks** | [**List[ChecklistTask]**](ChecklistTask.md) | List of tasks in the checklist | 
**others_can_add_tasks** | **bool** | *Optional*. *True*, if users other than the creator of the list can add tasks to the list | [optional] [default to True]
**others_can_mark_tasks_as_done** | **bool** | *Optional*. *True*, if users other than the creator of the list can mark tasks as done or not done | [optional] [default to True]

## Example

```python
from tele_rest.models.checklist import Checklist

# TODO update the JSON string below
json = "{}"
# create an instance of Checklist from a JSON string
checklist_instance = Checklist.from_json(json)
# print the JSON string representation of the object
print(Checklist.to_json())

# convert the object into a dict
checklist_dict = checklist_instance.to_dict()
# create an instance of Checklist from a dict
checklist_from_dict = Checklist.from_dict(checklist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


