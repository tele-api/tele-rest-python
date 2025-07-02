# GetUpdatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[Update]**](Update.md) |  | 

## Example

```python
from tele_rest.models.get_updates_response import GetUpdatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUpdatesResponse from a JSON string
get_updates_response_instance = GetUpdatesResponse.from_json(json)
# print the JSON string representation of the object
print(GetUpdatesResponse.to_json())

# convert the object into a dict
get_updates_response_dict = get_updates_response_instance.to_dict()
# create an instance of GetUpdatesResponse from a dict
get_updates_response_from_dict = GetUpdatesResponse.from_dict(get_updates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


