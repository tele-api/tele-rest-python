# PostEditForumTopicRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostRestrictChatMemberRequestChatId**](PostRestrictChatMemberRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread of the forum topic | 
**name** | **str** | New topic name, 0-128 characters. If not specified or empty, the current name of the topic will be kept | [optional] 
**icon_custom_emoji_id** | **str** | New unique identifier of the custom emoji shown as the topic icon. Use [getForumTopicIconStickers](https://core.telegram.org/bots/api/#getforumtopiciconstickers) to get all allowed custom emoji identifiers. Pass an empty string to remove the icon. If not specified, the current icon will be kept | [optional] 

## Example

```python
from tele_rest.models.post_edit_forum_topic_request import PostEditForumTopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostEditForumTopicRequest from a JSON string
post_edit_forum_topic_request_instance = PostEditForumTopicRequest.from_json(json)
# print the JSON string representation of the object
print(PostEditForumTopicRequest.to_json())

# convert the object into a dict
post_edit_forum_topic_request_dict = post_edit_forum_topic_request_instance.to_dict()
# create an instance of PostEditForumTopicRequest from a dict
post_edit_forum_topic_request_from_dict = PostEditForumTopicRequest.from_dict(post_edit_forum_topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


