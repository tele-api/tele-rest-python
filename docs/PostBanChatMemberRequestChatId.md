# PostBanChatMemberRequestChatId

Unique identifier for the target group or username of the target supergroup or channel (in the format `@channelusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_ban_chat_member_request_chat_id import PostBanChatMemberRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of PostBanChatMemberRequestChatId from a JSON string
post_ban_chat_member_request_chat_id_instance = PostBanChatMemberRequestChatId.from_json(json)
# print the JSON string representation of the object
print(PostBanChatMemberRequestChatId.to_json())

# convert the object into a dict
post_ban_chat_member_request_chat_id_dict = post_ban_chat_member_request_chat_id_instance.to_dict()
# create an instance of PostBanChatMemberRequestChatId from a dict
post_ban_chat_member_request_chat_id_from_dict = PostBanChatMemberRequestChatId.from_dict(post_ban_chat_member_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


