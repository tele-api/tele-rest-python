# GetMyDescriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**BotDescription**](BotDescription.md) |  | 

## Example

```python
from tele_rest.models.get_my_description_response import GetMyDescriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyDescriptionResponse from a JSON string
get_my_description_response_instance = GetMyDescriptionResponse.from_json(json)
# print the JSON string representation of the object
print(GetMyDescriptionResponse.to_json())

# convert the object into a dict
get_my_description_response_dict = get_my_description_response_instance.to_dict()
# create an instance of GetMyDescriptionResponse from a dict
get_my_description_response_from_dict = GetMyDescriptionResponse.from_dict(get_my_description_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


