# GetMyDefaultAdministratorRightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**ChatAdministratorRights**](ChatAdministratorRights.md) |  | 

## Example

```python
from tele_rest.models.get_my_default_administrator_rights_response import GetMyDefaultAdministratorRightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyDefaultAdministratorRightsResponse from a JSON string
get_my_default_administrator_rights_response_instance = GetMyDefaultAdministratorRightsResponse.from_json(json)
# print the JSON string representation of the object
print(GetMyDefaultAdministratorRightsResponse.to_json())

# convert the object into a dict
get_my_default_administrator_rights_response_dict = get_my_default_administrator_rights_response_instance.to_dict()
# create an instance of GetMyDefaultAdministratorRightsResponse from a dict
get_my_default_administrator_rights_response_from_dict = GetMyDefaultAdministratorRightsResponse.from_dict(get_my_default_administrator_rights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


