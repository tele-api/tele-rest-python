# GetChatMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**ChatMember**](ChatMember.md) |  | 

## Example

```python
from tele_rest.models.get_chat_member_response import GetChatMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatMemberResponse from a JSON string
get_chat_member_response_instance = GetChatMemberResponse.from_json(json)
# print the JSON string representation of the object
print(GetChatMemberResponse.to_json())

# convert the object into a dict
get_chat_member_response_dict = get_chat_member_response_instance.to_dict()
# create an instance of GetChatMemberResponse from a dict
get_chat_member_response_from_dict = GetChatMemberResponse.from_dict(get_chat_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


