# GetMyShortDescriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**BotShortDescription**](BotShortDescription.md) |  | 

## Example

```python
from tele_rest.models.get_my_short_description_response import GetMyShortDescriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyShortDescriptionResponse from a JSON string
get_my_short_description_response_instance = GetMyShortDescriptionResponse.from_json(json)
# print the JSON string representation of the object
print(GetMyShortDescriptionResponse.to_json())

# convert the object into a dict
get_my_short_description_response_dict = get_my_short_description_response_instance.to_dict()
# create an instance of GetMyShortDescriptionResponse from a dict
get_my_short_description_response_from_dict = GetMyShortDescriptionResponse.from_dict(get_my_short_description_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


