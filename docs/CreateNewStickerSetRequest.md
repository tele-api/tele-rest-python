# CreateNewStickerSetRequest

Request parameters for createNewStickerSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User identifier of created sticker set owner | 
**name** | **str** | Short name of sticker set, to be used in &#x60;t.me/addstickers/&#x60; URLs (e.g., *animals*). Can contain only English letters, digits and underscores. Must begin with a letter, can&#39;t contain consecutive underscores and must end in &#x60;\&quot;_by_&lt;bot_username&gt;\&quot;&#x60;. &#x60;&lt;bot_username&gt;&#x60; is case insensitive. 1-64 characters. | 
**title** | **str** | Sticker set title, 1-64 characters | 
**stickers** | [**List[InputSticker]**](InputSticker.md) | A JSON-serialized list of 1-50 initial stickers to be added to the sticker set | 
**sticker_type** | **str** | Type of stickers in the set, pass “regular”, “mask”, or “custom\\_emoji”. By default, a regular sticker set is created. | [optional] 
**needs_repainting** | **bool** | Pass *True* if stickers in the sticker set must be repainted to the color of text when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context; for custom emoji sticker sets only | [optional] 

## Example

```python
from tele_rest.models.create_new_sticker_set_request import CreateNewStickerSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewStickerSetRequest from a JSON string
create_new_sticker_set_request_instance = CreateNewStickerSetRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNewStickerSetRequest.to_json())

# convert the object into a dict
create_new_sticker_set_request_dict = create_new_sticker_set_request_instance.to_dict()
# create an instance of CreateNewStickerSetRequest from a dict
create_new_sticker_set_request_from_dict = CreateNewStickerSetRequest.from_dict(create_new_sticker_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


