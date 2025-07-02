# RemoveBusinessAccountProfilePhotoRequest

Request parameters for removeBusinessAccountProfilePhoto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**is_public** | **bool** | Pass True to remove the public photo, which is visible even if the main photo is hidden by the business account&#39;s privacy settings. After the main photo is removed, the previous profile photo (if present) becomes the main photo. | [optional] 

## Example

```python
from tele_rest.models.remove_business_account_profile_photo_request import RemoveBusinessAccountProfilePhotoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveBusinessAccountProfilePhotoRequest from a JSON string
remove_business_account_profile_photo_request_instance = RemoveBusinessAccountProfilePhotoRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveBusinessAccountProfilePhotoRequest.to_json())

# convert the object into a dict
remove_business_account_profile_photo_request_dict = remove_business_account_profile_photo_request_instance.to_dict()
# create an instance of RemoveBusinessAccountProfilePhotoRequest from a dict
remove_business_account_profile_photo_request_from_dict = RemoveBusinessAccountProfilePhotoRequest.from_dict(remove_business_account_profile_photo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


