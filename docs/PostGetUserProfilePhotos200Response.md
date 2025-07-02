# PostGetUserProfilePhotos200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**UserProfilePhotos**](UserProfilePhotos.md) |  | 

## Example

```python
from tele_rest.models.post_get_user_profile_photos200_response import PostGetUserProfilePhotos200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetUserProfilePhotos200Response from a JSON string
post_get_user_profile_photos200_response_instance = PostGetUserProfilePhotos200Response.from_json(json)
# print the JSON string representation of the object
print(PostGetUserProfilePhotos200Response.to_json())

# convert the object into a dict
post_get_user_profile_photos200_response_dict = post_get_user_profile_photos200_response_instance.to_dict()
# create an instance of PostGetUserProfilePhotos200Response from a dict
post_get_user_profile_photos200_response_from_dict = PostGetUserProfilePhotos200Response.from_dict(post_get_user_profile_photos200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


