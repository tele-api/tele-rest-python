# InputStoryContentPhoto

Describes a photo to post as a story.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the content, must be *photo* | [default to 'photo']
**photo** | **str** | The photo to post as a story. The photo must be of the size 1080x1920 and must not exceed 10 MB. The photo can&#39;t be reused and can only be uploaded as a new file, so you can pass “attach://\\&lt;file\\_attach\\_name\\&gt;” if the photo was uploaded using multipart/form-data under \\&lt;file\\_attach\\_name\\&gt;. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files) | 

## Example

```python
from tele_rest.models.input_story_content_photo import InputStoryContentPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of InputStoryContentPhoto from a JSON string
input_story_content_photo_instance = InputStoryContentPhoto.from_json(json)
# print the JSON string representation of the object
print(InputStoryContentPhoto.to_json())

# convert the object into a dict
input_story_content_photo_dict = input_story_content_photo_instance.to_dict()
# create an instance of InputStoryContentPhoto from a dict
input_story_content_photo_from_dict = InputStoryContentPhoto.from_dict(input_story_content_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


