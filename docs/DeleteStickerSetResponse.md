# DeleteStickerSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.delete_sticker_set_response import DeleteStickerSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteStickerSetResponse from a JSON string
delete_sticker_set_response_instance = DeleteStickerSetResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteStickerSetResponse.to_json())

# convert the object into a dict
delete_sticker_set_response_dict = delete_sticker_set_response_instance.to_dict()
# create an instance of DeleteStickerSetResponse from a dict
delete_sticker_set_response_from_dict = DeleteStickerSetResponse.from_dict(delete_sticker_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


