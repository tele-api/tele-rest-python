# GetChatMemberCountRequest

Request parameters for getChatMemberCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**GetChatRequestChatId**](GetChatRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.get_chat_member_count_request import GetChatMemberCountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatMemberCountRequest from a JSON string
get_chat_member_count_request_instance = GetChatMemberCountRequest.from_json(json)
# print the JSON string representation of the object
print(GetChatMemberCountRequest.to_json())

# convert the object into a dict
get_chat_member_count_request_dict = get_chat_member_count_request_instance.to_dict()
# create an instance of GetChatMemberCountRequest from a dict
get_chat_member_count_request_from_dict = GetChatMemberCountRequest.from_dict(get_chat_member_count_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


