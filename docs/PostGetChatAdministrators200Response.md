# PostGetChatAdministrators200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[ChatMember]**](ChatMember.md) |  | 

## Example

```python
from tele_rest.models.post_get_chat_administrators200_response import PostGetChatAdministrators200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetChatAdministrators200Response from a JSON string
post_get_chat_administrators200_response_instance = PostGetChatAdministrators200Response.from_json(json)
# print the JSON string representation of the object
print(PostGetChatAdministrators200Response.to_json())

# convert the object into a dict
post_get_chat_administrators200_response_dict = post_get_chat_administrators200_response_instance.to_dict()
# create an instance of PostGetChatAdministrators200Response from a dict
post_get_chat_administrators200_response_from_dict = PostGetChatAdministrators200Response.from_dict(post_get_chat_administrators200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


