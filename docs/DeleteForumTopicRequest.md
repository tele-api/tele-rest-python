# DeleteForumTopicRequest

Request parameters for deleteForumTopic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberRequestChatId**](RestrictChatMemberRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread of the forum topic | 

## Example

```python
from tele_rest.models.delete_forum_topic_request import DeleteForumTopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteForumTopicRequest from a JSON string
delete_forum_topic_request_instance = DeleteForumTopicRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteForumTopicRequest.to_json())

# convert the object into a dict
delete_forum_topic_request_dict = delete_forum_topic_request_instance.to_dict()
# create an instance of DeleteForumTopicRequest from a dict
delete_forum_topic_request_from_dict = DeleteForumTopicRequest.from_dict(delete_forum_topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


