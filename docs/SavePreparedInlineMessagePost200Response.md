# SavePreparedInlineMessagePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**PreparedInlineMessage**](PreparedInlineMessage.md) |  | 

## Example

```python
from tele_rest.models.save_prepared_inline_message_post200_response import SavePreparedInlineMessagePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SavePreparedInlineMessagePost200Response from a JSON string
save_prepared_inline_message_post200_response_instance = SavePreparedInlineMessagePost200Response.from_json(json)
# print the JSON string representation of the object
print(SavePreparedInlineMessagePost200Response.to_json())

# convert the object into a dict
save_prepared_inline_message_post200_response_dict = save_prepared_inline_message_post200_response_instance.to_dict()
# create an instance of SavePreparedInlineMessagePost200Response from a dict
save_prepared_inline_message_post200_response_from_dict = SavePreparedInlineMessagePost200Response.from_dict(save_prepared_inline_message_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


