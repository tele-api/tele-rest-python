# Animation

This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | Identifier for this file, which can be used to download or reuse the file | 
**file_unique_id** | **str** | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can&#39;t be used to download or reuse the file. | 
**width** | **int** | Video width as defined by the sender | 
**height** | **int** | Video height as defined by the sender | 
**duration** | **int** | Duration of the video in seconds as defined by the sender | 
**thumbnail** | [**PhotoSize**](PhotoSize.md) |  | [optional] 
**file_name** | **str** | *Optional*. Original animation filename as defined by the sender | [optional] 
**mime_type** | **str** | *Optional*. MIME type of the file as defined by the sender | [optional] 
**file_size** | **int** | *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. | [optional] 

## Example

```python
from tele_rest.models.animation import Animation

# TODO update the JSON string below
json = "{}"
# create an instance of Animation from a JSON string
animation_instance = Animation.from_json(json)
# print the JSON string representation of the object
print(Animation.to_json())

# convert the object into a dict
animation_dict = animation_instance.to_dict()
# create an instance of Animation from a dict
animation_from_dict = Animation.from_dict(animation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


