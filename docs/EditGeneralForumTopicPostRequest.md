# EditGeneralForumTopicPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberPostRequestChatId**](RestrictChatMemberPostRequestChatId.md) |  | 
**name** | **str** | New topic name, 1-128 characters | 

## Example

```python
from tele_rest.models.edit_general_forum_topic_post_request import EditGeneralForumTopicPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditGeneralForumTopicPostRequest from a JSON string
edit_general_forum_topic_post_request_instance = EditGeneralForumTopicPostRequest.from_json(json)
# print the JSON string representation of the object
print(EditGeneralForumTopicPostRequest.to_json())

# convert the object into a dict
edit_general_forum_topic_post_request_dict = edit_general_forum_topic_post_request_instance.to_dict()
# create an instance of EditGeneralForumTopicPostRequest from a dict
edit_general_forum_topic_post_request_from_dict = EditGeneralForumTopicPostRequest.from_dict(edit_general_forum_topic_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


