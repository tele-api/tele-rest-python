# PostEditGeneralForumTopicRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostRestrictChatMemberRequestChatId**](PostRestrictChatMemberRequestChatId.md) |  | 
**name** | **str** | New topic name, 1-128 characters | 

## Example

```python
from tele_rest.models.post_edit_general_forum_topic_request import PostEditGeneralForumTopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostEditGeneralForumTopicRequest from a JSON string
post_edit_general_forum_topic_request_instance = PostEditGeneralForumTopicRequest.from_json(json)
# print the JSON string representation of the object
print(PostEditGeneralForumTopicRequest.to_json())

# convert the object into a dict
post_edit_general_forum_topic_request_dict = post_edit_general_forum_topic_request_instance.to_dict()
# create an instance of PostEditGeneralForumTopicRequest from a dict
post_edit_general_forum_topic_request_from_dict = PostEditGeneralForumTopicRequest.from_dict(post_edit_general_forum_topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


