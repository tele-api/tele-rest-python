# CloseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.close_response import CloseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloseResponse from a JSON string
close_response_instance = CloseResponse.from_json(json)
# print the JSON string representation of the object
print(CloseResponse.to_json())

# convert the object into a dict
close_response_dict = close_response_instance.to_dict()
# create an instance of CloseResponse from a dict
close_response_from_dict = CloseResponse.from_dict(close_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


