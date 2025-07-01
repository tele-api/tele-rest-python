# SetStickerKeywordsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticker** | **str** | File identifier of the sticker | 
**keywords** | **List[str]** | A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters | [optional] 

## Example

```python
from tele_rest.models.set_sticker_keywords_post_request import SetStickerKeywordsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetStickerKeywordsPostRequest from a JSON string
set_sticker_keywords_post_request_instance = SetStickerKeywordsPostRequest.from_json(json)
# print the JSON string representation of the object
print(SetStickerKeywordsPostRequest.to_json())

# convert the object into a dict
set_sticker_keywords_post_request_dict = set_sticker_keywords_post_request_instance.to_dict()
# create an instance of SetStickerKeywordsPostRequest from a dict
set_sticker_keywords_post_request_from_dict = SetStickerKeywordsPostRequest.from_dict(set_sticker_keywords_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


