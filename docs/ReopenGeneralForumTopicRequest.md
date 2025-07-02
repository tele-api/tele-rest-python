# ReopenGeneralForumTopicRequest

Request parameters for reopenGeneralForumTopic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**BotCommandScopeChatChatId**](BotCommandScopeChatChatId.md) |  | 

## Example

```python
from tele_rest.models.reopen_general_forum_topic_request import ReopenGeneralForumTopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReopenGeneralForumTopicRequest from a JSON string
reopen_general_forum_topic_request_instance = ReopenGeneralForumTopicRequest.from_json(json)
# print the JSON string representation of the object
print(ReopenGeneralForumTopicRequest.to_json())

# convert the object into a dict
reopen_general_forum_topic_request_dict = reopen_general_forum_topic_request_instance.to_dict()
# create an instance of ReopenGeneralForumTopicRequest from a dict
reopen_general_forum_topic_request_from_dict = ReopenGeneralForumTopicRequest.from_dict(reopen_general_forum_topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


