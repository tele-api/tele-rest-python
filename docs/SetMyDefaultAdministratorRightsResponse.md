# SetMyDefaultAdministratorRightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_my_default_administrator_rights_response import SetMyDefaultAdministratorRightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetMyDefaultAdministratorRightsResponse from a JSON string
set_my_default_administrator_rights_response_instance = SetMyDefaultAdministratorRightsResponse.from_json(json)
# print the JSON string representation of the object
print(SetMyDefaultAdministratorRightsResponse.to_json())

# convert the object into a dict
set_my_default_administrator_rights_response_dict = set_my_default_administrator_rights_response_instance.to_dict()
# create an instance of SetMyDefaultAdministratorRightsResponse from a dict
set_my_default_administrator_rights_response_from_dict = SetMyDefaultAdministratorRightsResponse.from_dict(set_my_default_administrator_rights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


