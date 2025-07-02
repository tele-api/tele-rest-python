# PostCloseForumTopicRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostRestrictChatMemberRequestChatId**](PostRestrictChatMemberRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread of the forum topic | 

## Example

```python
from tele_rest.models.post_close_forum_topic_request import PostCloseForumTopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCloseForumTopicRequest from a JSON string
post_close_forum_topic_request_instance = PostCloseForumTopicRequest.from_json(json)
# print the JSON string representation of the object
print(PostCloseForumTopicRequest.to_json())

# convert the object into a dict
post_close_forum_topic_request_dict = post_close_forum_topic_request_instance.to_dict()
# create an instance of PostCloseForumTopicRequest from a dict
post_close_forum_topic_request_from_dict = PostCloseForumTopicRequest.from_dict(post_close_forum_topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


