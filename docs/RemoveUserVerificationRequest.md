# RemoveUserVerificationRequest

Request parameters for removeUserVerification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.remove_user_verification_request import RemoveUserVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveUserVerificationRequest from a JSON string
remove_user_verification_request_instance = RemoveUserVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveUserVerificationRequest.to_json())

# convert the object into a dict
remove_user_verification_request_dict = remove_user_verification_request_instance.to_dict()
# create an instance of RemoveUserVerificationRequest from a dict
remove_user_verification_request_from_dict = RemoveUserVerificationRequest.from_dict(remove_user_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


