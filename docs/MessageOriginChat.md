# MessageOriginChat

The message was originally sent on behalf of a chat to a group chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the message origin, always “chat” | [default to 'chat']
**var_date** | **int** | Date the message was sent originally in Unix time | 
**sender_chat** | [**Chat**](Chat.md) |  | 
**author_signature** | **str** | *Optional*. For messages originally sent by an anonymous chat administrator, original message author signature | [optional] 

## Example

```python
from tele_rest.models.message_origin_chat import MessageOriginChat

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOriginChat from a JSON string
message_origin_chat_instance = MessageOriginChat.from_json(json)
# print the JSON string representation of the object
print(MessageOriginChat.to_json())

# convert the object into a dict
message_origin_chat_dict = message_origin_chat_instance.to_dict()
# create an instance of MessageOriginChat from a dict
message_origin_chat_from_dict = MessageOriginChat.from_dict(message_origin_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


