# RemoveBusinessAccountProfilePhotoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.remove_business_account_profile_photo_response import RemoveBusinessAccountProfilePhotoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveBusinessAccountProfilePhotoResponse from a JSON string
remove_business_account_profile_photo_response_instance = RemoveBusinessAccountProfilePhotoResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveBusinessAccountProfilePhotoResponse.to_json())

# convert the object into a dict
remove_business_account_profile_photo_response_dict = remove_business_account_profile_photo_response_instance.to_dict()
# create an instance of RemoveBusinessAccountProfilePhotoResponse from a dict
remove_business_account_profile_photo_response_from_dict = RemoveBusinessAccountProfilePhotoResponse.from_dict(remove_business_account_profile_photo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


