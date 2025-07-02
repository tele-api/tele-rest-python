# SetBusinessAccountUsernameRequest

Request parameters for setBusinessAccountUsername

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**username** | **str** | The new value of the username for the business account; 0-32 characters | [optional] 

## Example

```python
from tele_rest.models.set_business_account_username_request import SetBusinessAccountUsernameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetBusinessAccountUsernameRequest from a JSON string
set_business_account_username_request_instance = SetBusinessAccountUsernameRequest.from_json(json)
# print the JSON string representation of the object
print(SetBusinessAccountUsernameRequest.to_json())

# convert the object into a dict
set_business_account_username_request_dict = set_business_account_username_request_instance.to_dict()
# create an instance of SetBusinessAccountUsernameRequest from a dict
set_business_account_username_request_from_dict = SetBusinessAccountUsernameRequest.from_dict(set_business_account_username_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


