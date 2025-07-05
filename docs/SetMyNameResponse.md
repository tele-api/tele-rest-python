# SetMyNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_my_name_response import SetMyNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetMyNameResponse from a JSON string
set_my_name_response_instance = SetMyNameResponse.from_json(json)
# print the JSON string representation of the object
print(SetMyNameResponse.to_json())

# convert the object into a dict
set_my_name_response_dict = set_my_name_response_instance.to_dict()
# create an instance of SetMyNameResponse from a dict
set_my_name_response_from_dict = SetMyNameResponse.from_dict(set_my_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


