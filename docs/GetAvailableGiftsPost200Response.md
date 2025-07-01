# GetAvailableGiftsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Gifts**](Gifts.md) |  | 

## Example

```python
from tele_rest.models.get_available_gifts_post200_response import GetAvailableGiftsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailableGiftsPost200Response from a JSON string
get_available_gifts_post200_response_instance = GetAvailableGiftsPost200Response.from_json(json)
# print the JSON string representation of the object
print(GetAvailableGiftsPost200Response.to_json())

# convert the object into a dict
get_available_gifts_post200_response_dict = get_available_gifts_post200_response_instance.to_dict()
# create an instance of GetAvailableGiftsPost200Response from a dict
get_available_gifts_post200_response_from_dict = GetAvailableGiftsPost200Response.from_dict(get_available_gifts_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


