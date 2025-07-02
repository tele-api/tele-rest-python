# GetUserProfilePhotosResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**UserProfilePhotos**](UserProfilePhotos.md) |  | 

## Example

```python
from tele_rest.models.get_user_profile_photos_response import GetUserProfilePhotosResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserProfilePhotosResponse from a JSON string
get_user_profile_photos_response_instance = GetUserProfilePhotosResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserProfilePhotosResponse.to_json())

# convert the object into a dict
get_user_profile_photos_response_dict = get_user_profile_photos_response_instance.to_dict()
# create an instance of GetUserProfilePhotosResponse from a dict
get_user_profile_photos_response_from_dict = GetUserProfilePhotosResponse.from_dict(get_user_profile_photos_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


