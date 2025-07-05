# SendStickerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_sticker_response import SendStickerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendStickerResponse from a JSON string
send_sticker_response_instance = SendStickerResponse.from_json(json)
# print the JSON string representation of the object
print(SendStickerResponse.to_json())

# convert the object into a dict
send_sticker_response_dict = send_sticker_response_instance.to_dict()
# create an instance of SendStickerResponse from a dict
send_sticker_response_from_dict = SendStickerResponse.from_dict(send_sticker_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


