# UnbanChatMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.unban_chat_member_response import UnbanChatMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnbanChatMemberResponse from a JSON string
unban_chat_member_response_instance = UnbanChatMemberResponse.from_json(json)
# print the JSON string representation of the object
print(UnbanChatMemberResponse.to_json())

# convert the object into a dict
unban_chat_member_response_dict = unban_chat_member_response_instance.to_dict()
# create an instance of UnbanChatMemberResponse from a dict
unban_chat_member_response_from_dict = UnbanChatMemberResponse.from_dict(unban_chat_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


