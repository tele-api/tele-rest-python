# PostRestrictChatMemberRequestChatId

Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_restrict_chat_member_request_chat_id import PostRestrictChatMemberRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of PostRestrictChatMemberRequestChatId from a JSON string
post_restrict_chat_member_request_chat_id_instance = PostRestrictChatMemberRequestChatId.from_json(json)
# print the JSON string representation of the object
print(PostRestrictChatMemberRequestChatId.to_json())

# convert the object into a dict
post_restrict_chat_member_request_chat_id_dict = post_restrict_chat_member_request_chat_id_instance.to_dict()
# create an instance of PostRestrictChatMemberRequestChatId from a dict
post_restrict_chat_member_request_chat_id_from_dict = PostRestrictChatMemberRequestChatId.from_dict(post_restrict_chat_member_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


