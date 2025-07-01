# MessageOriginChannel

The message was originally sent to a channel chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the message origin, always “channel” | [default to 'channel']
**var_date** | **int** | Date the message was sent originally in Unix time | 
**chat** | [**Chat**](Chat.md) |  | 
**message_id** | **int** | Unique message identifier inside the chat | 
**author_signature** | **str** | *Optional*. Signature of the original post author | [optional] 

## Example

```python
from tele_rest.models.message_origin_channel import MessageOriginChannel

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOriginChannel from a JSON string
message_origin_channel_instance = MessageOriginChannel.from_json(json)
# print the JSON string representation of the object
print(MessageOriginChannel.to_json())

# convert the object into a dict
message_origin_channel_dict = message_origin_channel_instance.to_dict()
# create an instance of MessageOriginChannel from a dict
message_origin_channel_from_dict = MessageOriginChannel.from_dict(message_origin_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


