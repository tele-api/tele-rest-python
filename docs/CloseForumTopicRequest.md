# CloseForumTopicRequest

Request parameters for closeForumTopic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberRequestChatId**](RestrictChatMemberRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread of the forum topic | 

## Example

```python
from tele_rest.models.close_forum_topic_request import CloseForumTopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloseForumTopicRequest from a JSON string
close_forum_topic_request_instance = CloseForumTopicRequest.from_json(json)
# print the JSON string representation of the object
print(CloseForumTopicRequest.to_json())

# convert the object into a dict
close_forum_topic_request_dict = close_forum_topic_request_instance.to_dict()
# create an instance of CloseForumTopicRequest from a dict
close_forum_topic_request_from_dict = CloseForumTopicRequest.from_dict(close_forum_topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


