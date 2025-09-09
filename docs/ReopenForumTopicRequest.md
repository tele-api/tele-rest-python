# ReopenForumTopicRequest

Request parameters for reopenForumTopic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberRequestChatId**](RestrictChatMemberRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread of the forum topic | 

## Example

```python
from tele_rest.models.reopen_forum_topic_request import ReopenForumTopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReopenForumTopicRequest from a JSON string
reopen_forum_topic_request_instance = ReopenForumTopicRequest.from_json(json)
# print the JSON string representation of the object
print(ReopenForumTopicRequest.to_json())

# convert the object into a dict
reopen_forum_topic_request_dict = reopen_forum_topic_request_instance.to_dict()
# create an instance of ReopenForumTopicRequest from a dict
reopen_forum_topic_request_from_dict = ReopenForumTopicRequest.from_dict(reopen_forum_topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


