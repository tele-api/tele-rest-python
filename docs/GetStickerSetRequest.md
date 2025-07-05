# GetStickerSetRequest

Request parameters for getStickerSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the sticker set | 

## Example

```python
from tele_rest.models.get_sticker_set_request import GetStickerSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStickerSetRequest from a JSON string
get_sticker_set_request_instance = GetStickerSetRequest.from_json(json)
# print the JSON string representation of the object
print(GetStickerSetRequest.to_json())

# convert the object into a dict
get_sticker_set_request_dict = get_sticker_set_request_instance.to_dict()
# create an instance of GetStickerSetRequest from a dict
get_sticker_set_request_from_dict = GetStickerSetRequest.from_dict(get_sticker_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


