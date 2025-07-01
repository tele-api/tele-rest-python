# SetStickerSetTitlePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sticker set name | 
**title** | **str** | Sticker set title, 1-64 characters | 

## Example

```python
from tele_rest.models.set_sticker_set_title_post_request import SetStickerSetTitlePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetStickerSetTitlePostRequest from a JSON string
set_sticker_set_title_post_request_instance = SetStickerSetTitlePostRequest.from_json(json)
# print the JSON string representation of the object
print(SetStickerSetTitlePostRequest.to_json())

# convert the object into a dict
set_sticker_set_title_post_request_dict = set_sticker_set_title_post_request_instance.to_dict()
# create an instance of SetStickerSetTitlePostRequest from a dict
set_sticker_set_title_post_request_from_dict = SetStickerSetTitlePostRequest.from_dict(set_sticker_set_title_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


