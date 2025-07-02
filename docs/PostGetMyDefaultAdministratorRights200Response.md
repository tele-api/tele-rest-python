# PostGetMyDefaultAdministratorRights200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**ChatAdministratorRights**](ChatAdministratorRights.md) |  | 

## Example

```python
from tele_rest.models.post_get_my_default_administrator_rights200_response import PostGetMyDefaultAdministratorRights200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetMyDefaultAdministratorRights200Response from a JSON string
post_get_my_default_administrator_rights200_response_instance = PostGetMyDefaultAdministratorRights200Response.from_json(json)
# print the JSON string representation of the object
print(PostGetMyDefaultAdministratorRights200Response.to_json())

# convert the object into a dict
post_get_my_default_administrator_rights200_response_dict = post_get_my_default_administrator_rights200_response_instance.to_dict()
# create an instance of PostGetMyDefaultAdministratorRights200Response from a dict
post_get_my_default_administrator_rights200_response_from_dict = PostGetMyDefaultAdministratorRights200Response.from_dict(post_get_my_default_administrator_rights200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


