# UnbanChatMemberRequest

Request parameters for unbanChatMember

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**BanChatMemberRequestChatId**](BanChatMemberRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 
**only_if_banned** | **bool** | Do nothing if the user is not banned | [optional] 

## Example

```python
from tele_rest.models.unban_chat_member_request import UnbanChatMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnbanChatMemberRequest from a JSON string
unban_chat_member_request_instance = UnbanChatMemberRequest.from_json(json)
# print the JSON string representation of the object
print(UnbanChatMemberRequest.to_json())

# convert the object into a dict
unban_chat_member_request_dict = unban_chat_member_request_instance.to_dict()
# create an instance of UnbanChatMemberRequest from a dict
unban_chat_member_request_from_dict = UnbanChatMemberRequest.from_dict(unban_chat_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


