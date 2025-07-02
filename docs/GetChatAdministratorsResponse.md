# GetChatAdministratorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[ChatMember]**](ChatMember.md) |  | 

## Example

```python
from tele_rest.models.get_chat_administrators_response import GetChatAdministratorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatAdministratorsResponse from a JSON string
get_chat_administrators_response_instance = GetChatAdministratorsResponse.from_json(json)
# print the JSON string representation of the object
print(GetChatAdministratorsResponse.to_json())

# convert the object into a dict
get_chat_administrators_response_dict = get_chat_administrators_response_instance.to_dict()
# create an instance of GetChatAdministratorsResponse from a dict
get_chat_administrators_response_from_dict = GetChatAdministratorsResponse.from_dict(get_chat_administrators_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


