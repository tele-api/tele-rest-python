# AddStickerToSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.add_sticker_to_set_response import AddStickerToSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddStickerToSetResponse from a JSON string
add_sticker_to_set_response_instance = AddStickerToSetResponse.from_json(json)
# print the JSON string representation of the object
print(AddStickerToSetResponse.to_json())

# convert the object into a dict
add_sticker_to_set_response_dict = add_sticker_to_set_response_instance.to_dict()
# create an instance of AddStickerToSetResponse from a dict
add_sticker_to_set_response_from_dict = AddStickerToSetResponse.from_dict(add_sticker_to_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


