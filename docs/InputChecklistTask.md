# InputChecklistTask

Describes a task to add to a checklist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the task; must be positive and unique among all task identifiers currently present in the checklist | 
**text** | **str** | Text of the task; 1-100 characters after entities parsing | 
**parse_mode** | **str** | Optional. Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. | [optional] 
**text_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the text, which can be specified instead of parse\\_mode. Currently, only *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, and *custom\\_emoji* entities are allowed. | [optional] 

## Example

```python
from tele_rest.models.input_checklist_task import InputChecklistTask

# TODO update the JSON string below
json = "{}"
# create an instance of InputChecklistTask from a JSON string
input_checklist_task_instance = InputChecklistTask.from_json(json)
# print the JSON string representation of the object
print(InputChecklistTask.to_json())

# convert the object into a dict
input_checklist_task_dict = input_checklist_task_instance.to_dict()
# create an instance of InputChecklistTask from a dict
input_checklist_task_from_dict = InputChecklistTask.from_dict(input_checklist_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


