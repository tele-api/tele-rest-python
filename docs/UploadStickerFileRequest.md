# UploadStickerFileRequest

Request parameters for uploadStickerFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User identifier of sticker file owner | 
**sticker** | **object** |  | 
**sticker_format** | **str** | Format of the sticker, must be one of “static”, “animated”, “video” | 

## Example

```python
from tele_rest.models.upload_sticker_file_request import UploadStickerFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadStickerFileRequest from a JSON string
upload_sticker_file_request_instance = UploadStickerFileRequest.from_json(json)
# print the JSON string representation of the object
print(UploadStickerFileRequest.to_json())

# convert the object into a dict
upload_sticker_file_request_dict = upload_sticker_file_request_instance.to_dict()
# create an instance of UploadStickerFileRequest from a dict
upload_sticker_file_request_from_dict = UploadStickerFileRequest.from_dict(upload_sticker_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


