# CreateNewStickerSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.create_new_sticker_set_response import CreateNewStickerSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewStickerSetResponse from a JSON string
create_new_sticker_set_response_instance = CreateNewStickerSetResponse.from_json(json)
# print the JSON string representation of the object
print(CreateNewStickerSetResponse.to_json())

# convert the object into a dict
create_new_sticker_set_response_dict = create_new_sticker_set_response_instance.to_dict()
# create an instance of CreateNewStickerSetResponse from a dict
create_new_sticker_set_response_from_dict = CreateNewStickerSetResponse.from_dict(create_new_sticker_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


