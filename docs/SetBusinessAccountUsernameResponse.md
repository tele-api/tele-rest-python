# SetBusinessAccountUsernameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_business_account_username_response import SetBusinessAccountUsernameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetBusinessAccountUsernameResponse from a JSON string
set_business_account_username_response_instance = SetBusinessAccountUsernameResponse.from_json(json)
# print the JSON string representation of the object
print(SetBusinessAccountUsernameResponse.to_json())

# convert the object into a dict
set_business_account_username_response_dict = set_business_account_username_response_instance.to_dict()
# create an instance of SetBusinessAccountUsernameResponse from a dict
set_business_account_username_response_from_dict = SetBusinessAccountUsernameResponse.from_dict(set_business_account_username_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


