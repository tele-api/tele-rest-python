# PinChatMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.pin_chat_message_response import PinChatMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PinChatMessageResponse from a JSON string
pin_chat_message_response_instance = PinChatMessageResponse.from_json(json)
# print the JSON string representation of the object
print(PinChatMessageResponse.to_json())

# convert the object into a dict
pin_chat_message_response_dict = pin_chat_message_response_instance.to_dict()
# create an instance of PinChatMessageResponse from a dict
pin_chat_message_response_from_dict = PinChatMessageResponse.from_dict(pin_chat_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


