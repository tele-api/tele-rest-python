# BanChatMemberRequestChatId

Unique identifier for the target group or username of the target supergroup or channel (in the format `@channelusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.ban_chat_member_request_chat_id import BanChatMemberRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of BanChatMemberRequestChatId from a JSON string
ban_chat_member_request_chat_id_instance = BanChatMemberRequestChatId.from_json(json)
# print the JSON string representation of the object
print(BanChatMemberRequestChatId.to_json())

# convert the object into a dict
ban_chat_member_request_chat_id_dict = ban_chat_member_request_chat_id_instance.to_dict()
# create an instance of BanChatMemberRequestChatId from a dict
ban_chat_member_request_chat_id_from_dict = BanChatMemberRequestChatId.from_dict(ban_chat_member_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


