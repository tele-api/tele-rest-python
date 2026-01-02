# UnpinAllForumTopicMessagesRequest

Request parameters for unpinAllForumTopicMessages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberRequestChatId**](RestrictChatMemberRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread of the forum topic | 

## Example

```python
from tele_rest.models.unpin_all_forum_topic_messages_request import UnpinAllForumTopicMessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnpinAllForumTopicMessagesRequest from a JSON string
unpin_all_forum_topic_messages_request_instance = UnpinAllForumTopicMessagesRequest.from_json(json)
# print the JSON string representation of the object
print(UnpinAllForumTopicMessagesRequest.to_json())

# convert the object into a dict
unpin_all_forum_topic_messages_request_dict = unpin_all_forum_topic_messages_request_instance.to_dict()
# create an instance of UnpinAllForumTopicMessagesRequest from a dict
unpin_all_forum_topic_messages_request_from_dict = UnpinAllForumTopicMessagesRequest.from_dict(unpin_all_forum_topic_messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


