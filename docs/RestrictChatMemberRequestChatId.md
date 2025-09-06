# RestrictChatMemberRequestChatId

Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.restrict_chat_member_request_chat_id import RestrictChatMemberRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictChatMemberRequestChatId from a JSON string
restrict_chat_member_request_chat_id_instance = RestrictChatMemberRequestChatId.from_json(json)
# print the JSON string representation of the object
print(RestrictChatMemberRequestChatId.to_json())

# convert the object into a dict
restrict_chat_member_request_chat_id_dict = restrict_chat_member_request_chat_id_instance.to_dict()
# create an instance of RestrictChatMemberRequestChatId from a dict
restrict_chat_member_request_chat_id_from_dict = RestrictChatMemberRequestChatId.from_dict(restrict_chat_member_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


