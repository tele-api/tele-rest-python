# EditMessageCaptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**EditMessageTextResponseResult**](EditMessageTextResponseResult.md) |  | 

## Example

```python
from tele_rest.models.edit_message_caption_response import EditMessageCaptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageCaptionResponse from a JSON string
edit_message_caption_response_instance = EditMessageCaptionResponse.from_json(json)
# print the JSON string representation of the object
print(EditMessageCaptionResponse.to_json())

# convert the object into a dict
edit_message_caption_response_dict = edit_message_caption_response_instance.to_dict()
# create an instance of EditMessageCaptionResponse from a dict
edit_message_caption_response_from_dict = EditMessageCaptionResponse.from_dict(edit_message_caption_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


