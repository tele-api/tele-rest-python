# PostGetChatMemberCount200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **int** |  | 

## Example

```python
from tele_rest.models.post_get_chat_member_count200_response import PostGetChatMemberCount200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetChatMemberCount200Response from a JSON string
post_get_chat_member_count200_response_instance = PostGetChatMemberCount200Response.from_json(json)
# print the JSON string representation of the object
print(PostGetChatMemberCount200Response.to_json())

# convert the object into a dict
post_get_chat_member_count200_response_dict = post_get_chat_member_count200_response_instance.to_dict()
# create an instance of PostGetChatMemberCount200Response from a dict
post_get_chat_member_count200_response_from_dict = PostGetChatMemberCount200Response.from_dict(post_get_chat_member_count200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


