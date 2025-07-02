# UploadStickerFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**File**](File.md) |  | 

## Example

```python
from tele_rest.models.upload_sticker_file_response import UploadStickerFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadStickerFileResponse from a JSON string
upload_sticker_file_response_instance = UploadStickerFileResponse.from_json(json)
# print the JSON string representation of the object
print(UploadStickerFileResponse.to_json())

# convert the object into a dict
upload_sticker_file_response_dict = upload_sticker_file_response_instance.to_dict()
# create an instance of UploadStickerFileResponse from a dict
upload_sticker_file_response_from_dict = UploadStickerFileResponse.from_dict(upload_sticker_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


