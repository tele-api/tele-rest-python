# PostGetUserChatBoostsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostGetUserChatBoostsRequestChatId**](PostGetUserChatBoostsRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.post_get_user_chat_boosts_request import PostGetUserChatBoostsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetUserChatBoostsRequest from a JSON string
post_get_user_chat_boosts_request_instance = PostGetUserChatBoostsRequest.from_json(json)
# print the JSON string representation of the object
print(PostGetUserChatBoostsRequest.to_json())

# convert the object into a dict
post_get_user_chat_boosts_request_dict = post_get_user_chat_boosts_request_instance.to_dict()
# create an instance of PostGetUserChatBoostsRequest from a dict
post_get_user_chat_boosts_request_from_dict = PostGetUserChatBoostsRequest.from_dict(post_get_user_chat_boosts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


