# RestrictChatMemberPostRequestChatId

Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.restrict_chat_member_post_request_chat_id import RestrictChatMemberPostRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictChatMemberPostRequestChatId from a JSON string
restrict_chat_member_post_request_chat_id_instance = RestrictChatMemberPostRequestChatId.from_json(json)
# print the JSON string representation of the object
print(RestrictChatMemberPostRequestChatId.to_json())

# convert the object into a dict
restrict_chat_member_post_request_chat_id_dict = restrict_chat_member_post_request_chat_id_instance.to_dict()
# create an instance of RestrictChatMemberPostRequestChatId from a dict
restrict_chat_member_post_request_chat_id_from_dict = RestrictChatMemberPostRequestChatId.from_dict(restrict_chat_member_post_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


