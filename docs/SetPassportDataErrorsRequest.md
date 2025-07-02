# SetPassportDataErrorsRequest

Request parameters for setPassportDataErrors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User identifier | 
**errors** | [**List[PassportElementError]**](PassportElementError.md) | A JSON-serialized array describing the errors | 

## Example

```python
from tele_rest.models.set_passport_data_errors_request import SetPassportDataErrorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetPassportDataErrorsRequest from a JSON string
set_passport_data_errors_request_instance = SetPassportDataErrorsRequest.from_json(json)
# print the JSON string representation of the object
print(SetPassportDataErrorsRequest.to_json())

# convert the object into a dict
set_passport_data_errors_request_dict = set_passport_data_errors_request_instance.to_dict()
# create an instance of SetPassportDataErrorsRequest from a dict
set_passport_data_errors_request_from_dict = SetPassportDataErrorsRequest.from_dict(set_passport_data_errors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


