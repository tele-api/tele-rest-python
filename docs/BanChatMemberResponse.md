# BanChatMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.ban_chat_member_response import BanChatMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BanChatMemberResponse from a JSON string
ban_chat_member_response_instance = BanChatMemberResponse.from_json(json)
# print the JSON string representation of the object
print(BanChatMemberResponse.to_json())

# convert the object into a dict
ban_chat_member_response_dict = ban_chat_member_response_instance.to_dict()
# create an instance of BanChatMemberResponse from a dict
ban_chat_member_response_from_dict = BanChatMemberResponse.from_dict(ban_chat_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


