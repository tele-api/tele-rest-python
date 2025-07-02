# GetMyDefaultAdministratorRightsRequest

Request parameters for getMyDefaultAdministratorRights

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_channels** | **bool** | Pass *True* to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned. | [optional] 

## Example

```python
from tele_rest.models.get_my_default_administrator_rights_request import GetMyDefaultAdministratorRightsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyDefaultAdministratorRightsRequest from a JSON string
get_my_default_administrator_rights_request_instance = GetMyDefaultAdministratorRightsRequest.from_json(json)
# print the JSON string representation of the object
print(GetMyDefaultAdministratorRightsRequest.to_json())

# convert the object into a dict
get_my_default_administrator_rights_request_dict = get_my_default_administrator_rights_request_instance.to_dict()
# create an instance of GetMyDefaultAdministratorRightsRequest from a dict
get_my_default_administrator_rights_request_from_dict = GetMyDefaultAdministratorRightsRequest.from_dict(get_my_default_administrator_rights_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


