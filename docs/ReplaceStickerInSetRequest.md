# ReplaceStickerInSetRequest

Request parameters for replaceStickerInSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User identifier of the sticker set owner | 
**name** | **str** | Sticker set name | 
**old_sticker** | **str** | File identifier of the replaced sticker | 
**sticker** | [**InputSticker**](InputSticker.md) |  | 

## Example

```python
from tele_rest.models.replace_sticker_in_set_request import ReplaceStickerInSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceStickerInSetRequest from a JSON string
replace_sticker_in_set_request_instance = ReplaceStickerInSetRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceStickerInSetRequest.to_json())

# convert the object into a dict
replace_sticker_in_set_request_dict = replace_sticker_in_set_request_instance.to_dict()
# create an instance of ReplaceStickerInSetRequest from a dict
replace_sticker_in_set_request_from_dict = ReplaceStickerInSetRequest.from_dict(replace_sticker_in_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


