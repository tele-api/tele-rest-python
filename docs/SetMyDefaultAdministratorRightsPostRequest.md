# SetMyDefaultAdministratorRightsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rights** | [**ChatAdministratorRights**](ChatAdministratorRights.md) |  | [optional] 
**for_channels** | **bool** | Pass *True* to change the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be changed. | [optional] 

## Example

```python
from tele_rest.models.set_my_default_administrator_rights_post_request import SetMyDefaultAdministratorRightsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetMyDefaultAdministratorRightsPostRequest from a JSON string
set_my_default_administrator_rights_post_request_instance = SetMyDefaultAdministratorRightsPostRequest.from_json(json)
# print the JSON string representation of the object
print(SetMyDefaultAdministratorRightsPostRequest.to_json())

# convert the object into a dict
set_my_default_administrator_rights_post_request_dict = set_my_default_administrator_rights_post_request_instance.to_dict()
# create an instance of SetMyDefaultAdministratorRightsPostRequest from a dict
set_my_default_administrator_rights_post_request_from_dict = SetMyDefaultAdministratorRightsPostRequest.from_dict(set_my_default_administrator_rights_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


