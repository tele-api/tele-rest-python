# BanChatMemberRequest

Request parameters for banChatMember

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**BanChatMemberRequestChatId**](BanChatMemberRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 
**until_date** | **int** | Date when the user will be unbanned; Unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only. | [optional] 
**revoke_messages** | **bool** | Pass *True* to delete all messages from the chat for the user that is being removed. If *False*, the user will be able to see messages in the group that were sent before the user was removed. Always *True* for supergroups and channels. | [optional] 

## Example

```python
from tele_rest.models.ban_chat_member_request import BanChatMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BanChatMemberRequest from a JSON string
ban_chat_member_request_instance = BanChatMemberRequest.from_json(json)
# print the JSON string representation of the object
print(BanChatMemberRequest.to_json())

# convert the object into a dict
ban_chat_member_request_dict = ban_chat_member_request_instance.to_dict()
# create an instance of BanChatMemberRequest from a dict
ban_chat_member_request_from_dict = BanChatMemberRequest.from_dict(ban_chat_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


