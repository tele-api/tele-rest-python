# SavePreparedInlineMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**PreparedInlineMessage**](PreparedInlineMessage.md) |  | 

## Example

```python
from tele_rest.models.save_prepared_inline_message_response import SavePreparedInlineMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SavePreparedInlineMessageResponse from a JSON string
save_prepared_inline_message_response_instance = SavePreparedInlineMessageResponse.from_json(json)
# print the JSON string representation of the object
print(SavePreparedInlineMessageResponse.to_json())

# convert the object into a dict
save_prepared_inline_message_response_dict = save_prepared_inline_message_response_instance.to_dict()
# create an instance of SavePreparedInlineMessageResponse from a dict
save_prepared_inline_message_response_from_dict = SavePreparedInlineMessageResponse.from_dict(save_prepared_inline_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


