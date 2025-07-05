# GetMyNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**BotName**](BotName.md) |  | 

## Example

```python
from tele_rest.models.get_my_name_response import GetMyNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyNameResponse from a JSON string
get_my_name_response_instance = GetMyNameResponse.from_json(json)
# print the JSON string representation of the object
print(GetMyNameResponse.to_json())

# convert the object into a dict
get_my_name_response_dict = get_my_name_response_instance.to_dict()
# create an instance of GetMyNameResponse from a dict
get_my_name_response_from_dict = GetMyNameResponse.from_dict(get_my_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


