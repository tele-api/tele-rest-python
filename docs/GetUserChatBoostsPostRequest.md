# GetUserChatBoostsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**GetUserChatBoostsPostRequestChatId**](GetUserChatBoostsPostRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.get_user_chat_boosts_post_request import GetUserChatBoostsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserChatBoostsPostRequest from a JSON string
get_user_chat_boosts_post_request_instance = GetUserChatBoostsPostRequest.from_json(json)
# print the JSON string representation of the object
print(GetUserChatBoostsPostRequest.to_json())

# convert the object into a dict
get_user_chat_boosts_post_request_dict = get_user_chat_boosts_post_request_instance.to_dict()
# create an instance of GetUserChatBoostsPostRequest from a dict
get_user_chat_boosts_post_request_from_dict = GetUserChatBoostsPostRequest.from_dict(get_user_chat_boosts_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


