# SetStickerKeywordsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_sticker_keywords_response import SetStickerKeywordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetStickerKeywordsResponse from a JSON string
set_sticker_keywords_response_instance = SetStickerKeywordsResponse.from_json(json)
# print the JSON string representation of the object
print(SetStickerKeywordsResponse.to_json())

# convert the object into a dict
set_sticker_keywords_response_dict = set_sticker_keywords_response_instance.to_dict()
# create an instance of SetStickerKeywordsResponse from a dict
set_sticker_keywords_response_from_dict = SetStickerKeywordsResponse.from_dict(set_sticker_keywords_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


