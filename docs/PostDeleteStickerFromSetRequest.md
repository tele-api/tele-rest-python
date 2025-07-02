# PostDeleteStickerFromSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticker** | **str** | File identifier of the sticker | 

## Example

```python
from tele_rest.models.post_delete_sticker_from_set_request import PostDeleteStickerFromSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteStickerFromSetRequest from a JSON string
post_delete_sticker_from_set_request_instance = PostDeleteStickerFromSetRequest.from_json(json)
# print the JSON string representation of the object
print(PostDeleteStickerFromSetRequest.to_json())

# convert the object into a dict
post_delete_sticker_from_set_request_dict = post_delete_sticker_from_set_request_instance.to_dict()
# create an instance of PostDeleteStickerFromSetRequest from a dict
post_delete_sticker_from_set_request_from_dict = PostDeleteStickerFromSetRequest.from_dict(post_delete_sticker_from_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


