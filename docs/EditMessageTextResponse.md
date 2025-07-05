# EditMessageTextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**EditMessageTextResponseResult**](EditMessageTextResponseResult.md) |  | 

## Example

```python
from tele_rest.models.edit_message_text_response import EditMessageTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageTextResponse from a JSON string
edit_message_text_response_instance = EditMessageTextResponse.from_json(json)
# print the JSON string representation of the object
print(EditMessageTextResponse.to_json())

# convert the object into a dict
edit_message_text_response_dict = edit_message_text_response_instance.to_dict()
# create an instance of EditMessageTextResponse from a dict
edit_message_text_response_from_dict = EditMessageTextResponse.from_dict(edit_message_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


