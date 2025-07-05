# GetStickerSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**StickerSet**](StickerSet.md) |  | 

## Example

```python
from tele_rest.models.get_sticker_set_response import GetStickerSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStickerSetResponse from a JSON string
get_sticker_set_response_instance = GetStickerSetResponse.from_json(json)
# print the JSON string representation of the object
print(GetStickerSetResponse.to_json())

# convert the object into a dict
get_sticker_set_response_dict = get_sticker_set_response_instance.to_dict()
# create an instance of GetStickerSetResponse from a dict
get_sticker_set_response_from_dict = GetStickerSetResponse.from_dict(get_sticker_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


