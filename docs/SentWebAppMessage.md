# SentWebAppMessage

Describes an inline message sent by a [Web App](https://core.telegram.org/bots/webapps) on behalf of a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline_message_id** | **str** | *Optional*. Identifier of the sent inline message. Available only if there is an [inline keyboard](https://core.telegram.org/bots/api/#inlinekeyboardmarkup) attached to the message. | [optional] 

## Example

```python
from tele_rest.models.sent_web_app_message import SentWebAppMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SentWebAppMessage from a JSON string
sent_web_app_message_instance = SentWebAppMessage.from_json(json)
# print the JSON string representation of the object
print(SentWebAppMessage.to_json())

# convert the object into a dict
sent_web_app_message_dict = sent_web_app_message_instance.to_dict()
# create an instance of SentWebAppMessage from a dict
sent_web_app_message_from_dict = SentWebAppMessage.from_dict(sent_web_app_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


