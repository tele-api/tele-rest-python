# GetMyDescriptionPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**BotDescription**](BotDescription.md) |  | 

## Example

```python
from tele_rest.models.get_my_description_post200_response import GetMyDescriptionPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyDescriptionPost200Response from a JSON string
get_my_description_post200_response_instance = GetMyDescriptionPost200Response.from_json(json)
# print the JSON string representation of the object
print(GetMyDescriptionPost200Response.to_json())

# convert the object into a dict
get_my_description_post200_response_dict = get_my_description_post200_response_instance.to_dict()
# create an instance of GetMyDescriptionPost200Response from a dict
get_my_description_post200_response_from_dict = GetMyDescriptionPost200Response.from_dict(get_my_description_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


