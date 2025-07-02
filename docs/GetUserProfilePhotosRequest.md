# GetUserProfilePhotosRequest

Request parameters for getUserProfilePhotos

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Unique identifier of the target user | 
**offset** | **int** | Sequential number of the first photo to be returned. By default, all photos are returned. | [optional] 
**limit** | **int** | Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100. | [optional] [default to 100]

## Example

```python
from tele_rest.models.get_user_profile_photos_request import GetUserProfilePhotosRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserProfilePhotosRequest from a JSON string
get_user_profile_photos_request_instance = GetUserProfilePhotosRequest.from_json(json)
# print the JSON string representation of the object
print(GetUserProfilePhotosRequest.to_json())

# convert the object into a dict
get_user_profile_photos_request_dict = get_user_profile_photos_request_instance.to_dict()
# create an instance of GetUserProfilePhotosRequest from a dict
get_user_profile_photos_request_from_dict = GetUserProfilePhotosRequest.from_dict(get_user_profile_photos_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


