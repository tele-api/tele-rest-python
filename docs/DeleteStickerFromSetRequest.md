# DeleteStickerFromSetRequest

Request parameters for deleteStickerFromSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticker** | **str** | File identifier of the sticker | 

## Example

```python
from tele_rest.models.delete_sticker_from_set_request import DeleteStickerFromSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteStickerFromSetRequest from a JSON string
delete_sticker_from_set_request_instance = DeleteStickerFromSetRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteStickerFromSetRequest.to_json())

# convert the object into a dict
delete_sticker_from_set_request_dict = delete_sticker_from_set_request_instance.to_dict()
# create an instance of DeleteStickerFromSetRequest from a dict
delete_sticker_from_set_request_from_dict = DeleteStickerFromSetRequest.from_dict(delete_sticker_from_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


