# EditMessageTextPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**EditMessageTextPost200ResponseResult**](EditMessageTextPost200ResponseResult.md) |  | 

## Example

```python
from tele_rest.models.edit_message_text_post200_response import EditMessageTextPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageTextPost200Response from a JSON string
edit_message_text_post200_response_instance = EditMessageTextPost200Response.from_json(json)
# print the JSON string representation of the object
print(EditMessageTextPost200Response.to_json())

# convert the object into a dict
edit_message_text_post200_response_dict = edit_message_text_post200_response_instance.to_dict()
# create an instance of EditMessageTextPost200Response from a dict
edit_message_text_post200_response_from_dict = EditMessageTextPost200Response.from_dict(edit_message_text_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


