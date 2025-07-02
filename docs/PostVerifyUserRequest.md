# PostVerifyUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Unique identifier of the target user | 
**custom_description** | **str** | Custom description for the verification; 0-70 characters. Must be empty if the organization isn&#39;t allowed to provide a custom verification description. | [optional] 

## Example

```python
from tele_rest.models.post_verify_user_request import PostVerifyUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostVerifyUserRequest from a JSON string
post_verify_user_request_instance = PostVerifyUserRequest.from_json(json)
# print the JSON string representation of the object
print(PostVerifyUserRequest.to_json())

# convert the object into a dict
post_verify_user_request_dict = post_verify_user_request_instance.to_dict()
# create an instance of PostVerifyUserRequest from a dict
post_verify_user_request_from_dict = PostVerifyUserRequest.from_dict(post_verify_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


