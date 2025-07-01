# GetUserChatBoostsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**UserChatBoosts**](UserChatBoosts.md) |  | 

## Example

```python
from tele_rest.models.get_user_chat_boosts_post200_response import GetUserChatBoostsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserChatBoostsPost200Response from a JSON string
get_user_chat_boosts_post200_response_instance = GetUserChatBoostsPost200Response.from_json(json)
# print the JSON string representation of the object
print(GetUserChatBoostsPost200Response.to_json())

# convert the object into a dict
get_user_chat_boosts_post200_response_dict = get_user_chat_boosts_post200_response_instance.to_dict()
# create an instance of GetUserChatBoostsPost200Response from a dict
get_user_chat_boosts_post200_response_from_dict = GetUserChatBoostsPost200Response.from_dict(get_user_chat_boosts_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


