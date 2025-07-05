# VerifyUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.verify_user_response import VerifyUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyUserResponse from a JSON string
verify_user_response_instance = VerifyUserResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyUserResponse.to_json())

# convert the object into a dict
verify_user_response_dict = verify_user_response_instance.to_dict()
# create an instance of VerifyUserResponse from a dict
verify_user_response_from_dict = VerifyUserResponse.from_dict(verify_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


