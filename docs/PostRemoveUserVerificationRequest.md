# PostRemoveUserVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.post_remove_user_verification_request import PostRemoveUserVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRemoveUserVerificationRequest from a JSON string
post_remove_user_verification_request_instance = PostRemoveUserVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(PostRemoveUserVerificationRequest.to_json())

# convert the object into a dict
post_remove_user_verification_request_dict = post_remove_user_verification_request_instance.to_dict()
# create an instance of PostRemoveUserVerificationRequest from a dict
post_remove_user_verification_request_from_dict = PostRemoveUserVerificationRequest.from_dict(post_remove_user_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


