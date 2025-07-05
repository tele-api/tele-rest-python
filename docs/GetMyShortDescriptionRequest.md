# GetMyShortDescriptionRequest

Request parameters for getMyShortDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_code** | **str** | A two-letter ISO 639-1 language code or an empty string | [optional] 

## Example

```python
from tele_rest.models.get_my_short_description_request import GetMyShortDescriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyShortDescriptionRequest from a JSON string
get_my_short_description_request_instance = GetMyShortDescriptionRequest.from_json(json)
# print the JSON string representation of the object
print(GetMyShortDescriptionRequest.to_json())

# convert the object into a dict
get_my_short_description_request_dict = get_my_short_description_request_instance.to_dict()
# create an instance of GetMyShortDescriptionRequest from a dict
get_my_short_description_request_from_dict = GetMyShortDescriptionRequest.from_dict(get_my_short_description_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


