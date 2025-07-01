# PaidMediaVideo

The paid media is a video.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the paid media, always “video” | [default to 'video']
**video** | [**Video**](Video.md) |  | 

## Example

```python
from tele_rest.models.paid_media_video import PaidMediaVideo

# TODO update the JSON string below
json = "{}"
# create an instance of PaidMediaVideo from a JSON string
paid_media_video_instance = PaidMediaVideo.from_json(json)
# print the JSON string representation of the object
print(PaidMediaVideo.to_json())

# convert the object into a dict
paid_media_video_dict = paid_media_video_instance.to_dict()
# create an instance of PaidMediaVideo from a dict
paid_media_video_from_dict = PaidMediaVideo.from_dict(paid_media_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


