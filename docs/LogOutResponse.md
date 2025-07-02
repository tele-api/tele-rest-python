# LogOutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.log_out_response import LogOutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogOutResponse from a JSON string
log_out_response_instance = LogOutResponse.from_json(json)
# print the JSON string representation of the object
print(LogOutResponse.to_json())

# convert the object into a dict
log_out_response_dict = log_out_response_instance.to_dict()
# create an instance of LogOutResponse from a dict
log_out_response_from_dict = LogOutResponse.from_dict(log_out_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


