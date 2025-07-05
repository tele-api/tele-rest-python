# HideGeneralForumTopicRequest

Request parameters for hideGeneralForumTopic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**BotCommandScopeChatChatId**](BotCommandScopeChatChatId.md) |  | 

## Example

```python
from tele_rest.models.hide_general_forum_topic_request import HideGeneralForumTopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HideGeneralForumTopicRequest from a JSON string
hide_general_forum_topic_request_instance = HideGeneralForumTopicRequest.from_json(json)
# print the JSON string representation of the object
print(HideGeneralForumTopicRequest.to_json())

# convert the object into a dict
hide_general_forum_topic_request_dict = hide_general_forum_topic_request_instance.to_dict()
# create an instance of HideGeneralForumTopicRequest from a dict
hide_general_forum_topic_request_from_dict = HideGeneralForumTopicRequest.from_dict(hide_general_forum_topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


