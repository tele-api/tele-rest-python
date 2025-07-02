# DeleteStickerSetRequest

Request parameters for deleteStickerSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sticker set name | 

## Example

```python
from tele_rest.models.delete_sticker_set_request import DeleteStickerSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteStickerSetRequest from a JSON string
delete_sticker_set_request_instance = DeleteStickerSetRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteStickerSetRequest.to_json())

# convert the object into a dict
delete_sticker_set_request_dict = delete_sticker_set_request_instance.to_dict()
# create an instance of DeleteStickerSetRequest from a dict
delete_sticker_set_request_from_dict = DeleteStickerSetRequest.from_dict(delete_sticker_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


