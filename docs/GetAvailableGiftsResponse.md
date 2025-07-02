# GetAvailableGiftsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Gifts**](Gifts.md) |  | 

## Example

```python
from tele_rest.models.get_available_gifts_response import GetAvailableGiftsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailableGiftsResponse from a JSON string
get_available_gifts_response_instance = GetAvailableGiftsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAvailableGiftsResponse.to_json())

# convert the object into a dict
get_available_gifts_response_dict = get_available_gifts_response_instance.to_dict()
# create an instance of GetAvailableGiftsResponse from a dict
get_available_gifts_response_from_dict = GetAvailableGiftsResponse.from_dict(get_available_gifts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


