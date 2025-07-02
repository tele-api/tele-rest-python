# PostSetStickerKeywordsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticker** | **str** | File identifier of the sticker | 
**keywords** | **List[str]** | A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters | [optional] 

## Example

```python
from tele_rest.models.post_set_sticker_keywords_request import PostSetStickerKeywordsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetStickerKeywordsRequest from a JSON string
post_set_sticker_keywords_request_instance = PostSetStickerKeywordsRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetStickerKeywordsRequest.to_json())

# convert the object into a dict
post_set_sticker_keywords_request_dict = post_set_sticker_keywords_request_instance.to_dict()
# create an instance of PostSetStickerKeywordsRequest from a dict
post_set_sticker_keywords_request_from_dict = PostSetStickerKeywordsRequest.from_dict(post_set_sticker_keywords_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


