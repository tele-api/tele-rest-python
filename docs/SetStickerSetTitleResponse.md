# SetStickerSetTitleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_sticker_set_title_response import SetStickerSetTitleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetStickerSetTitleResponse from a JSON string
set_sticker_set_title_response_instance = SetStickerSetTitleResponse.from_json(json)
# print the JSON string representation of the object
print(SetStickerSetTitleResponse.to_json())

# convert the object into a dict
set_sticker_set_title_response_dict = set_sticker_set_title_response_instance.to_dict()
# create an instance of SetStickerSetTitleResponse from a dict
set_sticker_set_title_response_from_dict = SetStickerSetTitleResponse.from_dict(set_sticker_set_title_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


