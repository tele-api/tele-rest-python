# ReplaceStickerInSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.replace_sticker_in_set_response import ReplaceStickerInSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceStickerInSetResponse from a JSON string
replace_sticker_in_set_response_instance = ReplaceStickerInSetResponse.from_json(json)
# print the JSON string representation of the object
print(ReplaceStickerInSetResponse.to_json())

# convert the object into a dict
replace_sticker_in_set_response_dict = replace_sticker_in_set_response_instance.to_dict()
# create an instance of ReplaceStickerInSetResponse from a dict
replace_sticker_in_set_response_from_dict = ReplaceStickerInSetResponse.from_dict(replace_sticker_in_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


