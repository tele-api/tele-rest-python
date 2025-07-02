# PostSetMyDefaultAdministratorRightsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rights** | [**ChatAdministratorRights**](ChatAdministratorRights.md) |  | [optional] 
**for_channels** | **bool** | Pass *True* to change the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be changed. | [optional] 

## Example

```python
from tele_rest.models.post_set_my_default_administrator_rights_request import PostSetMyDefaultAdministratorRightsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetMyDefaultAdministratorRightsRequest from a JSON string
post_set_my_default_administrator_rights_request_instance = PostSetMyDefaultAdministratorRightsRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetMyDefaultAdministratorRightsRequest.to_json())

# convert the object into a dict
post_set_my_default_administrator_rights_request_dict = post_set_my_default_administrator_rights_request_instance.to_dict()
# create an instance of PostSetMyDefaultAdministratorRightsRequest from a dict
post_set_my_default_administrator_rights_request_from_dict = PostSetMyDefaultAdministratorRightsRequest.from_dict(post_set_my_default_administrator_rights_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


