# InputProfilePhoto

This object describes a profile photo to set. Currently, it can be one of  * [InputProfilePhotoStatic](https://core.telegram.org/bots/api/#inputprofilephotostatic) * [InputProfilePhotoAnimated](https://core.telegram.org/bots/api/#inputprofilephotoanimated)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the profile photo, must be *animated* | [default to 'animated']
**photo** | **str** | The static profile photo. Profile photos can&#39;t be reused and can only be uploaded as a new file, so you can pass “attach://\\&lt;file\\_attach\\_name\\&gt;” if the photo was uploaded using multipart/form-data under \\&lt;file\\_attach\\_name\\&gt;. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files) | 
**animation** | **str** | The animated profile photo. Profile photos can&#39;t be reused and can only be uploaded as a new file, so you can pass “attach://\\&lt;file\\_attach\\_name\\&gt;” if the photo was uploaded using multipart/form-data under \\&lt;file\\_attach\\_name\\&gt;. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files) | 
**main_frame_timestamp** | **float** | *Optional*. Timestamp in seconds of the frame that will be used as the static profile photo. Defaults to 0.0. | [optional] 

## Example

```python
from tele_rest.models.input_profile_photo import InputProfilePhoto

# TODO update the JSON string below
json = "{}"
# create an instance of InputProfilePhoto from a JSON string
input_profile_photo_instance = InputProfilePhoto.from_json(json)
# print the JSON string representation of the object
print(InputProfilePhoto.to_json())

# convert the object into a dict
input_profile_photo_dict = input_profile_photo_instance.to_dict()
# create an instance of InputProfilePhoto from a dict
input_profile_photo_from_dict = InputProfilePhoto.from_dict(input_profile_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


