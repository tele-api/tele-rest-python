# GetBusinessAccountGiftsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**OwnedGifts**](OwnedGifts.md) |  | 

## Example

```python
from tele_rest.models.get_business_account_gifts_response import GetBusinessAccountGiftsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBusinessAccountGiftsResponse from a JSON string
get_business_account_gifts_response_instance = GetBusinessAccountGiftsResponse.from_json(json)
# print the JSON string representation of the object
print(GetBusinessAccountGiftsResponse.to_json())

# convert the object into a dict
get_business_account_gifts_response_dict = get_business_account_gifts_response_instance.to_dict()
# create an instance of GetBusinessAccountGiftsResponse from a dict
get_business_account_gifts_response_from_dict = GetBusinessAccountGiftsResponse.from_dict(get_business_account_gifts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


