# EditMessageReplyMarkupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**EditMessageTextResponseResult**](EditMessageTextResponseResult.md) |  | 

## Example

```python
from tele_rest.models.edit_message_reply_markup_response import EditMessageReplyMarkupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageReplyMarkupResponse from a JSON string
edit_message_reply_markup_response_instance = EditMessageReplyMarkupResponse.from_json(json)
# print the JSON string representation of the object
print(EditMessageReplyMarkupResponse.to_json())

# convert the object into a dict
edit_message_reply_markup_response_dict = edit_message_reply_markup_response_instance.to_dict()
# create an instance of EditMessageReplyMarkupResponse from a dict
edit_message_reply_markup_response_from_dict = EditMessageReplyMarkupResponse.from_dict(edit_message_reply_markup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


