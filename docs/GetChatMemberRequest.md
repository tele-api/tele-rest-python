# GetChatMemberRequest

Request parameters for getChatMember

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**GetChatRequestChatId**](GetChatRequestChatId.md) |  | 
**user_id** | **int** | Unique identifier of the target user | 

## Example

```python
from tele_rest.models.get_chat_member_request import GetChatMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatMemberRequest from a JSON string
get_chat_member_request_instance = GetChatMemberRequest.from_json(json)
# print the JSON string representation of the object
print(GetChatMemberRequest.to_json())

# convert the object into a dict
get_chat_member_request_dict = get_chat_member_request_instance.to_dict()
# create an instance of GetChatMemberRequest from a dict
get_chat_member_request_from_dict = GetChatMemberRequest.from_dict(get_chat_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


