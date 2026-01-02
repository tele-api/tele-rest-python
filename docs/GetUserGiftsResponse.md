# GetUserGiftsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**OwnedGifts**](OwnedGifts.md) |  | 

## Example

```python
from tele_rest.models.get_user_gifts_response import GetUserGiftsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserGiftsResponse from a JSON string
get_user_gifts_response_instance = GetUserGiftsResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserGiftsResponse.to_json())

# convert the object into a dict
get_user_gifts_response_dict = get_user_gifts_response_instance.to_dict()
# create an instance of GetUserGiftsResponse from a dict
get_user_gifts_response_from_dict = GetUserGiftsResponse.from_dict(get_user_gifts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


