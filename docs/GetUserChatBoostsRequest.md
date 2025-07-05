# GetUserChatBoostsRequest

Request parameters for getUserChatBoosts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**GetUserChatBoostsRequestChatId**](GetUserChatBoostsRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.get_user_chat_boosts_request import GetUserChatBoostsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserChatBoostsRequest from a JSON string
get_user_chat_boosts_request_instance = GetUserChatBoostsRequest.from_json(json)
# print the JSON string representation of the object
print(GetUserChatBoostsRequest.to_json())

# convert the object into a dict
get_user_chat_boosts_request_dict = get_user_chat_boosts_request_instance.to_dict()
# create an instance of GetUserChatBoostsRequest from a dict
get_user_chat_boosts_request_from_dict = GetUserChatBoostsRequest.from_dict(get_user_chat_boosts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


