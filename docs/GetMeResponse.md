# GetMeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**User**](User.md) |  | 

## Example

```python
from tele_rest.models.get_me_response import GetMeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMeResponse from a JSON string
get_me_response_instance = GetMeResponse.from_json(json)
# print the JSON string representation of the object
print(GetMeResponse.to_json())

# convert the object into a dict
get_me_response_dict = get_me_response_instance.to_dict()
# create an instance of GetMeResponse from a dict
get_me_response_from_dict = GetMeResponse.from_dict(get_me_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


