# CloseForumTopicPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberPostRequestChatId**](RestrictChatMemberPostRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread of the forum topic | 

## Example

```python
from tele_rest.models.close_forum_topic_post_request import CloseForumTopicPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloseForumTopicPostRequest from a JSON string
close_forum_topic_post_request_instance = CloseForumTopicPostRequest.from_json(json)
# print the JSON string representation of the object
print(CloseForumTopicPostRequest.to_json())

# convert the object into a dict
close_forum_topic_post_request_dict = close_forum_topic_post_request_instance.to_dict()
# create an instance of CloseForumTopicPostRequest from a dict
close_forum_topic_post_request_from_dict = CloseForumTopicPostRequest.from_dict(close_forum_topic_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


