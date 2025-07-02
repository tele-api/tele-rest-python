# SetBusinessAccountProfilePhotoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_business_account_profile_photo_response import SetBusinessAccountProfilePhotoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetBusinessAccountProfilePhotoResponse from a JSON string
set_business_account_profile_photo_response_instance = SetBusinessAccountProfilePhotoResponse.from_json(json)
# print the JSON string representation of the object
print(SetBusinessAccountProfilePhotoResponse.to_json())

# convert the object into a dict
set_business_account_profile_photo_response_dict = set_business_account_profile_photo_response_instance.to_dict()
# create an instance of SetBusinessAccountProfilePhotoResponse from a dict
set_business_account_profile_photo_response_from_dict = SetBusinessAccountProfilePhotoResponse.from_dict(set_business_account_profile_photo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


