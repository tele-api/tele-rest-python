# GetMyNameRequest

Request parameters for getMyName

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_code** | **str** | A two-letter ISO 639-1 language code or an empty string | [optional] 

## Example

```python
from tele_rest.models.get_my_name_request import GetMyNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyNameRequest from a JSON string
get_my_name_request_instance = GetMyNameRequest.from_json(json)
# print the JSON string representation of the object
print(GetMyNameRequest.to_json())

# convert the object into a dict
get_my_name_request_dict = get_my_name_request_instance.to_dict()
# create an instance of GetMyNameRequest from a dict
get_my_name_request_from_dict = GetMyNameRequest.from_dict(get_my_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


