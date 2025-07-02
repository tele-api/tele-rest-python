# UnbanChatSenderChatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.unban_chat_sender_chat_response import UnbanChatSenderChatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnbanChatSenderChatResponse from a JSON string
unban_chat_sender_chat_response_instance = UnbanChatSenderChatResponse.from_json(json)
# print the JSON string representation of the object
print(UnbanChatSenderChatResponse.to_json())

# convert the object into a dict
unban_chat_sender_chat_response_dict = unban_chat_sender_chat_response_instance.to_dict()
# create an instance of UnbanChatSenderChatResponse from a dict
unban_chat_sender_chat_response_from_dict = UnbanChatSenderChatResponse.from_dict(unban_chat_sender_chat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


