# MessageOrigin

This object describes the origin of a message. It can be one of  * [MessageOriginUser](https://core.telegram.org/bots/api/#messageoriginuser) * [MessageOriginHiddenUser](https://core.telegram.org/bots/api/#messageoriginhiddenuser) * [MessageOriginChat](https://core.telegram.org/bots/api/#messageoriginchat) * [MessageOriginChannel](https://core.telegram.org/bots/api/#messageoriginchannel)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the message origin, always “channel” | [default to 'channel']
**var_date** | **int** | Date the message was sent originally in Unix time | 
**sender_user** | [**User**](User.md) |  | 
**sender_user_name** | **str** | Name of the user that sent the message originally | 
**sender_chat** | [**Chat**](Chat.md) |  | 
**author_signature** | **str** | *Optional*. Signature of the original post author | [optional] 
**chat** | [**Chat**](Chat.md) |  | 
**message_id** | **int** | Unique message identifier inside the chat | 

## Example

```python
from tele_rest.models.message_origin import MessageOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOrigin from a JSON string
message_origin_instance = MessageOrigin.from_json(json)
# print the JSON string representation of the object
print(MessageOrigin.to_json())

# convert the object into a dict
message_origin_dict = message_origin_instance.to_dict()
# create an instance of MessageOrigin from a dict
message_origin_from_dict = MessageOrigin.from_dict(message_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


