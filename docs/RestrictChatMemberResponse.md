# RestrictChatMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.restrict_chat_member_response import RestrictChatMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictChatMemberResponse from a JSON string
restrict_chat_member_response_instance = RestrictChatMemberResponse.from_json(json)
# print the JSON string representation of the object
print(RestrictChatMemberResponse.to_json())

# convert the object into a dict
restrict_chat_member_response_dict = restrict_chat_member_response_instance.to_dict()
# create an instance of RestrictChatMemberResponse from a dict
restrict_chat_member_response_from_dict = RestrictChatMemberResponse.from_dict(restrict_chat_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


