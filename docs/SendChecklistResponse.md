# SendChecklistResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_checklist_response import SendChecklistResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendChecklistResponse from a JSON string
send_checklist_response_instance = SendChecklistResponse.from_json(json)
# print the JSON string representation of the object
print(SendChecklistResponse.to_json())

# convert the object into a dict
send_checklist_response_dict = send_checklist_response_instance.to_dict()
# create an instance of SendChecklistResponse from a dict
send_checklist_response_from_dict = SendChecklistResponse.from_dict(send_checklist_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


