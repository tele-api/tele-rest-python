# SetBusinessAccountProfilePhotoRequest

Request parameters for setBusinessAccountProfilePhoto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**photo** | [**InputProfilePhoto**](InputProfilePhoto.md) |  | 
**is_public** | **bool** | Pass *True* to set the public photo, which will be visible even if the main photo is hidden by the business account&#39;s privacy settings. An account can have only one public photo. | [optional] 

## Example

```python
from tele_rest.models.set_business_account_profile_photo_request import SetBusinessAccountProfilePhotoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetBusinessAccountProfilePhotoRequest from a JSON string
set_business_account_profile_photo_request_instance = SetBusinessAccountProfilePhotoRequest.from_json(json)
# print the JSON string representation of the object
print(SetBusinessAccountProfilePhotoRequest.to_json())

# convert the object into a dict
set_business_account_profile_photo_request_dict = set_business_account_profile_photo_request_instance.to_dict()
# create an instance of SetBusinessAccountProfilePhotoRequest from a dict
set_business_account_profile_photo_request_from_dict = SetBusinessAccountProfilePhotoRequest.from_dict(set_business_account_profile_photo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


