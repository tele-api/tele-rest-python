# InputStoryContentVideo

Describes a video to post as a story.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the content, must be *video* | [default to 'video']
**video** | **str** | The video to post as a story. The video must be of the size 720x1280, streamable, encoded with H.265 codec, with key frames added each second in the MPEG4 format, and must not exceed 30 MB. The video can&#39;t be reused and can only be uploaded as a new file, so you can pass “attach://\\&lt;file\\_attach\\_name\\&gt;” if the video was uploaded using multipart/form-data under \\&lt;file\\_attach\\_name\\&gt;. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files) | 
**duration** | **float** | *Optional*. Precise duration of the video in seconds; 0-60 | [optional] 
**cover_frame_timestamp** | **float** | *Optional*. Timestamp in seconds of the frame that will be used as the static cover for the story. Defaults to 0.0. | [optional] 
**is_animation** | **bool** | *Optional*. Pass *True* if the video has no sound | [optional] 

## Example

```python
from tele_rest.models.input_story_content_video import InputStoryContentVideo

# TODO update the JSON string below
json = "{}"
# create an instance of InputStoryContentVideo from a JSON string
input_story_content_video_instance = InputStoryContentVideo.from_json(json)
# print the JSON string representation of the object
print(InputStoryContentVideo.to_json())

# convert the object into a dict
input_story_content_video_dict = input_story_content_video_instance.to_dict()
# create an instance of InputStoryContentVideo from a dict
input_story_content_video_from_dict = InputStoryContentVideo.from_dict(input_story_content_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


