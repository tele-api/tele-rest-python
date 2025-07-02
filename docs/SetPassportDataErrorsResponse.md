# SetPassportDataErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_passport_data_errors_response import SetPassportDataErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetPassportDataErrorsResponse from a JSON string
set_passport_data_errors_response_instance = SetPassportDataErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(SetPassportDataErrorsResponse.to_json())

# convert the object into a dict
set_passport_data_errors_response_dict = set_passport_data_errors_response_instance.to_dict()
# create an instance of SetPassportDataErrorsResponse from a dict
set_passport_data_errors_response_from_dict = SetPassportDataErrorsResponse.from_dict(set_passport_data_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


