# DeleteStickerFromSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.delete_sticker_from_set_response import DeleteStickerFromSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteStickerFromSetResponse from a JSON string
delete_sticker_from_set_response_instance = DeleteStickerFromSetResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteStickerFromSetResponse.to_json())

# convert the object into a dict
delete_sticker_from_set_response_dict = delete_sticker_from_set_response_instance.to_dict()
# create an instance of DeleteStickerFromSetResponse from a dict
delete_sticker_from_set_response_from_dict = DeleteStickerFromSetResponse.from_dict(delete_sticker_from_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


