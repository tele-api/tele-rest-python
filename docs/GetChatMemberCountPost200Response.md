# GetChatMemberCountPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **int** |  | 

## Example

```python
from tele_rest.models.get_chat_member_count_post200_response import GetChatMemberCountPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatMemberCountPost200Response from a JSON string
get_chat_member_count_post200_response_instance = GetChatMemberCountPost200Response.from_json(json)
# print the JSON string representation of the object
print(GetChatMemberCountPost200Response.to_json())

# convert the object into a dict
get_chat_member_count_post200_response_dict = get_chat_member_count_post200_response_instance.to_dict()
# create an instance of GetChatMemberCountPost200Response from a dict
get_chat_member_count_post200_response_from_dict = GetChatMemberCountPost200Response.from_dict(get_chat_member_count_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


