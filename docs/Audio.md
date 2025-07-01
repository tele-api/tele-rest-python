# Audio

This object represents an audio file to be treated as music by the Telegram clients.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | Identifier for this file, which can be used to download or reuse the file | 
**file_unique_id** | **str** | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can&#39;t be used to download or reuse the file. | 
**duration** | **int** | Duration of the audio in seconds as defined by the sender | 
**performer** | **str** | *Optional*. Performer of the audio as defined by the sender or by audio tags | [optional] 
**title** | **str** | *Optional*. Title of the audio as defined by the sender or by audio tags | [optional] 
**file_name** | **str** | *Optional*. Original filename as defined by the sender | [optional] 
**mime_type** | **str** | *Optional*. MIME type of the file as defined by the sender | [optional] 
**file_size** | **int** | *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. | [optional] 
**thumbnail** | [**PhotoSize**](PhotoSize.md) |  | [optional] 

## Example

```python
from tele_rest.models.audio import Audio

# TODO update the JSON string below
json = "{}"
# create an instance of Audio from a JSON string
audio_instance = Audio.from_json(json)
# print the JSON string representation of the object
print(Audio.to_json())

# convert the object into a dict
audio_dict = audio_instance.to_dict()
# create an instance of Audio from a dict
audio_from_dict = Audio.from_dict(audio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


