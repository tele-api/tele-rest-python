# PostSetStickerPositionInSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticker** | **str** | File identifier of the sticker | 
**position** | **int** | New sticker position in the set, zero-based | 

## Example

```python
from tele_rest.models.post_set_sticker_position_in_set_request import PostSetStickerPositionInSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetStickerPositionInSetRequest from a JSON string
post_set_sticker_position_in_set_request_instance = PostSetStickerPositionInSetRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetStickerPositionInSetRequest.to_json())

# convert the object into a dict
post_set_sticker_position_in_set_request_dict = post_set_sticker_position_in_set_request_instance.to_dict()
# create an instance of PostSetStickerPositionInSetRequest from a dict
post_set_sticker_position_in_set_request_from_dict = PostSetStickerPositionInSetRequest.from_dict(post_set_sticker_position_in_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


