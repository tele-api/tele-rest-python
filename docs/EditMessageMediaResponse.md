# EditMessageMediaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**EditMessageTextResponseResult**](EditMessageTextResponseResult.md) |  | 

## Example

```python
from tele_rest.models.edit_message_media_response import EditMessageMediaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageMediaResponse from a JSON string
edit_message_media_response_instance = EditMessageMediaResponse.from_json(json)
# print the JSON string representation of the object
print(EditMessageMediaResponse.to_json())

# convert the object into a dict
edit_message_media_response_dict = edit_message_media_response_instance.to_dict()
# create an instance of EditMessageMediaResponse from a dict
edit_message_media_response_from_dict = EditMessageMediaResponse.from_dict(edit_message_media_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


