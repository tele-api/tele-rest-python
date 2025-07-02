# PostGetStickerSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the sticker set | 

## Example

```python
from tele_rest.models.post_get_sticker_set_request import PostGetStickerSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetStickerSetRequest from a JSON string
post_get_sticker_set_request_instance = PostGetStickerSetRequest.from_json(json)
# print the JSON string representation of the object
print(PostGetStickerSetRequest.to_json())

# convert the object into a dict
post_get_sticker_set_request_dict = post_get_sticker_set_request_instance.to_dict()
# create an instance of PostGetStickerSetRequest from a dict
post_get_sticker_set_request_from_dict = PostGetStickerSetRequest.from_dict(post_get_sticker_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


