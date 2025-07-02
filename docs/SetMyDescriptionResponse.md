# SetMyDescriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_my_description_response import SetMyDescriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetMyDescriptionResponse from a JSON string
set_my_description_response_instance = SetMyDescriptionResponse.from_json(json)
# print the JSON string representation of the object
print(SetMyDescriptionResponse.to_json())

# convert the object into a dict
set_my_description_response_dict = set_my_description_response_instance.to_dict()
# create an instance of SetMyDescriptionResponse from a dict
set_my_description_response_from_dict = SetMyDescriptionResponse.from_dict(set_my_description_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


