# PostGetUserChatBoosts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**UserChatBoosts**](UserChatBoosts.md) |  | 

## Example

```python
from tele_rest.models.post_get_user_chat_boosts200_response import PostGetUserChatBoosts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetUserChatBoosts200Response from a JSON string
post_get_user_chat_boosts200_response_instance = PostGetUserChatBoosts200Response.from_json(json)
# print the JSON string representation of the object
print(PostGetUserChatBoosts200Response.to_json())

# convert the object into a dict
post_get_user_chat_boosts200_response_dict = post_get_user_chat_boosts200_response_instance.to_dict()
# create an instance of PostGetUserChatBoosts200Response from a dict
post_get_user_chat_boosts200_response_from_dict = PostGetUserChatBoosts200Response.from_dict(post_get_user_chat_boosts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


