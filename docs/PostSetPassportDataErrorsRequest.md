# PostSetPassportDataErrorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User identifier | 
**errors** | [**List[PassportElementError]**](PassportElementError.md) | A JSON-serialized array describing the errors | 

## Example

```python
from tele_rest.models.post_set_passport_data_errors_request import PostSetPassportDataErrorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetPassportDataErrorsRequest from a JSON string
post_set_passport_data_errors_request_instance = PostSetPassportDataErrorsRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetPassportDataErrorsRequest.to_json())

# convert the object into a dict
post_set_passport_data_errors_request_dict = post_set_passport_data_errors_request_instance.to_dict()
# create an instance of PostSetPassportDataErrorsRequest from a dict
post_set_passport_data_errors_request_from_dict = PostSetPassportDataErrorsRequest.from_dict(post_set_passport_data_errors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


