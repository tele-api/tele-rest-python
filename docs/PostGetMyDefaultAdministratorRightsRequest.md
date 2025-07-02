# PostGetMyDefaultAdministratorRightsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_channels** | **bool** | Pass *True* to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned. | [optional] 

## Example

```python
from tele_rest.models.post_get_my_default_administrator_rights_request import PostGetMyDefaultAdministratorRightsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetMyDefaultAdministratorRightsRequest from a JSON string
post_get_my_default_administrator_rights_request_instance = PostGetMyDefaultAdministratorRightsRequest.from_json(json)
# print the JSON string representation of the object
print(PostGetMyDefaultAdministratorRightsRequest.to_json())

# convert the object into a dict
post_get_my_default_administrator_rights_request_dict = post_get_my_default_administrator_rights_request_instance.to_dict()
# create an instance of PostGetMyDefaultAdministratorRightsRequest from a dict
post_get_my_default_administrator_rights_request_from_dict = PostGetMyDefaultAdministratorRightsRequest.from_dict(post_get_my_default_administrator_rights_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


