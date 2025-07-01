# InputProfilePhotoAnimated

An animated profile photo in the MPEG4 format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the profile photo, must be *animated* | [default to 'animated']
**animation** | **str** | The animated profile photo. Profile photos can&#39;t be reused and can only be uploaded as a new file, so you can pass “attach://\\&lt;file\\_attach\\_name\\&gt;” if the photo was uploaded using multipart/form-data under \\&lt;file\\_attach\\_name\\&gt;. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files) | 
**main_frame_timestamp** | **float** | *Optional*. Timestamp in seconds of the frame that will be used as the static profile photo. Defaults to 0.0. | [optional] 

## Example

```python
from tele_rest.models.input_profile_photo_animated import InputProfilePhotoAnimated

# TODO update the JSON string below
json = "{}"
# create an instance of InputProfilePhotoAnimated from a JSON string
input_profile_photo_animated_instance = InputProfilePhotoAnimated.from_json(json)
# print the JSON string representation of the object
print(InputProfilePhotoAnimated.to_json())

# convert the object into a dict
input_profile_photo_animated_dict = input_profile_photo_animated_instance.to_dict()
# create an instance of InputProfilePhotoAnimated from a dict
input_profile_photo_animated_from_dict = InputProfilePhotoAnimated.from_dict(input_profile_photo_animated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


