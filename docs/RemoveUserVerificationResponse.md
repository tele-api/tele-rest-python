# RemoveUserVerificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.remove_user_verification_response import RemoveUserVerificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveUserVerificationResponse from a JSON string
remove_user_verification_response_instance = RemoveUserVerificationResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveUserVerificationResponse.to_json())

# convert the object into a dict
remove_user_verification_response_dict = remove_user_verification_response_instance.to_dict()
# create an instance of RemoveUserVerificationResponse from a dict
remove_user_verification_response_from_dict = RemoveUserVerificationResponse.from_dict(remove_user_verification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


