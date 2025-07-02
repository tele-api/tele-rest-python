# SendChatActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.send_chat_action_response import SendChatActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendChatActionResponse from a JSON string
send_chat_action_response_instance = SendChatActionResponse.from_json(json)
# print the JSON string representation of the object
print(SendChatActionResponse.to_json())

# convert the object into a dict
send_chat_action_response_dict = send_chat_action_response_instance.to_dict()
# create an instance of SendChatActionResponse from a dict
send_chat_action_response_from_dict = SendChatActionResponse.from_dict(send_chat_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


