# SetMyDescriptionRequest

Request parameters for setMyDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language. | [optional] 
**language_code** | **str** | A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for whose language there is no dedicated description. | [optional] 

## Example

```python
from tele_rest.models.set_my_description_request import SetMyDescriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetMyDescriptionRequest from a JSON string
set_my_description_request_instance = SetMyDescriptionRequest.from_json(json)
# print the JSON string representation of the object
print(SetMyDescriptionRequest.to_json())

# convert the object into a dict
set_my_description_request_dict = set_my_description_request_instance.to_dict()
# create an instance of SetMyDescriptionRequest from a dict
set_my_description_request_from_dict = SetMyDescriptionRequest.from_dict(set_my_description_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


