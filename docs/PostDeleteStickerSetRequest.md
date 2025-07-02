# PostDeleteStickerSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sticker set name | 

## Example

```python
from tele_rest.models.post_delete_sticker_set_request import PostDeleteStickerSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteStickerSetRequest from a JSON string
post_delete_sticker_set_request_instance = PostDeleteStickerSetRequest.from_json(json)
# print the JSON string representation of the object
print(PostDeleteStickerSetRequest.to_json())

# convert the object into a dict
post_delete_sticker_set_request_dict = post_delete_sticker_set_request_instance.to_dict()
# create an instance of PostDeleteStickerSetRequest from a dict
post_delete_sticker_set_request_from_dict = PostDeleteStickerSetRequest.from_dict(post_delete_sticker_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


