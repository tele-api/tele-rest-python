# ForceReply

Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice [privacy mode](https://core.telegram.org/bots/features#privacy-mode). Not supported in channels and for messages sent on behalf of a Telegram Business account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_reply** | **bool** | Shows reply interface to the user, as if they manually selected the bot&#39;s message and tapped &#39;Reply&#39; | [default to True]
**input_field_placeholder** | **str** | *Optional*. The placeholder to be shown in the input field when the reply is active; 1-64 characters | [optional] 
**selective** | **bool** | *Optional*. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the *text* of the [Message](https://core.telegram.org/bots/api/#message) object; 2) if the bot&#39;s message is a reply to a message in the same chat and forum topic, sender of the original message. | [optional] 

## Example

```python
from tele_rest.models.force_reply import ForceReply

# TODO update the JSON string below
json = "{}"
# create an instance of ForceReply from a JSON string
force_reply_instance = ForceReply.from_json(json)
# print the JSON string representation of the object
print(ForceReply.to_json())

# convert the object into a dict
force_reply_dict = force_reply_instance.to_dict()
# create an instance of ForceReply from a dict
force_reply_from_dict = ForceReply.from_dict(force_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


