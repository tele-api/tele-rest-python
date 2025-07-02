# PostCreateChatInviteLink200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**ChatInviteLink**](ChatInviteLink.md) |  | 

## Example

```python
from tele_rest.models.post_create_chat_invite_link200_response import PostCreateChatInviteLink200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateChatInviteLink200Response from a JSON string
post_create_chat_invite_link200_response_instance = PostCreateChatInviteLink200Response.from_json(json)
# print the JSON string representation of the object
print(PostCreateChatInviteLink200Response.to_json())

# convert the object into a dict
post_create_chat_invite_link200_response_dict = post_create_chat_invite_link200_response_instance.to_dict()
# create an instance of PostCreateChatInviteLink200Response from a dict
post_create_chat_invite_link200_response_from_dict = PostCreateChatInviteLink200Response.from_dict(post_create_chat_invite_link200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


