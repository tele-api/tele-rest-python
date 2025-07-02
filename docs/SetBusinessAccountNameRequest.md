# SetBusinessAccountNameRequest

Request parameters for setBusinessAccountName

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**first_name** | **str** | The new value of the first name for the business account; 1-64 characters | 
**last_name** | **str** | The new value of the last name for the business account; 0-64 characters | [optional] 

## Example

```python
from tele_rest.models.set_business_account_name_request import SetBusinessAccountNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetBusinessAccountNameRequest from a JSON string
set_business_account_name_request_instance = SetBusinessAccountNameRequest.from_json(json)
# print the JSON string representation of the object
print(SetBusinessAccountNameRequest.to_json())

# convert the object into a dict
set_business_account_name_request_dict = set_business_account_name_request_instance.to_dict()
# create an instance of SetBusinessAccountNameRequest from a dict
set_business_account_name_request_from_dict = SetBusinessAccountNameRequest.from_dict(set_business_account_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


