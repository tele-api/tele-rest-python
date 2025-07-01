# InputProfilePhotoStatic

A static profile photo in the .JPG format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the profile photo, must be *static* | [default to 'static']
**photo** | **str** | The static profile photo. Profile photos can&#39;t be reused and can only be uploaded as a new file, so you can pass “attach://\\&lt;file\\_attach\\_name\\&gt;” if the photo was uploaded using multipart/form-data under \\&lt;file\\_attach\\_name\\&gt;. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files) | 

## Example

```python
from tele_rest.models.input_profile_photo_static import InputProfilePhotoStatic

# TODO update the JSON string below
json = "{}"
# create an instance of InputProfilePhotoStatic from a JSON string
input_profile_photo_static_instance = InputProfilePhotoStatic.from_json(json)
# print the JSON string representation of the object
print(InputProfilePhotoStatic.to_json())

# convert the object into a dict
input_profile_photo_static_dict = input_profile_photo_static_instance.to_dict()
# create an instance of InputProfilePhotoStatic from a dict
input_profile_photo_static_from_dict = InputProfilePhotoStatic.from_dict(input_profile_photo_static_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


