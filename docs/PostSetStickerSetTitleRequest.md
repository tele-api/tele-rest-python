# PostSetStickerSetTitleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sticker set name | 
**title** | **str** | Sticker set title, 1-64 characters | 

## Example

```python
from tele_rest.models.post_set_sticker_set_title_request import PostSetStickerSetTitleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetStickerSetTitleRequest from a JSON string
post_set_sticker_set_title_request_instance = PostSetStickerSetTitleRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetStickerSetTitleRequest.to_json())

# convert the object into a dict
post_set_sticker_set_title_request_dict = post_set_sticker_set_title_request_instance.to_dict()
# create an instance of PostSetStickerSetTitleRequest from a dict
post_set_sticker_set_title_request_from_dict = PostSetStickerSetTitleRequest.from_dict(post_set_sticker_set_title_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


