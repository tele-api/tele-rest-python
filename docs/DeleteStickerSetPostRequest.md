# DeleteStickerSetPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sticker set name | 

## Example

```python
from tele_rest.models.delete_sticker_set_post_request import DeleteStickerSetPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteStickerSetPostRequest from a JSON string
delete_sticker_set_post_request_instance = DeleteStickerSetPostRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteStickerSetPostRequest.to_json())

# convert the object into a dict
delete_sticker_set_post_request_dict = delete_sticker_set_post_request_instance.to_dict()
# create an instance of DeleteStickerSetPostRequest from a dict
delete_sticker_set_post_request_from_dict = DeleteStickerSetPostRequest.from_dict(delete_sticker_set_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


