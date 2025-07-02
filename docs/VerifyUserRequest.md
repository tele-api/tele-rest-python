# VerifyUserRequest

Request parameters for verifyUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Unique identifier of the target user | 
**custom_description** | **str** | Custom description for the verification; 0-70 characters. Must be empty if the organization isn&#39;t allowed to provide a custom verification description. | [optional] 

## Example

```python
from tele_rest.models.verify_user_request import VerifyUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyUserRequest from a JSON string
verify_user_request_instance = VerifyUserRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyUserRequest.to_json())

# convert the object into a dict
verify_user_request_dict = verify_user_request_instance.to_dict()
# create an instance of VerifyUserRequest from a dict
verify_user_request_from_dict = VerifyUserRequest.from_dict(verify_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


