# EditGeneralForumTopicRequest

Request parameters for editGeneralForumTopic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberRequestChatId**](RestrictChatMemberRequestChatId.md) |  | 
**name** | **str** | New topic name, 1-128 characters | 

## Example

```python
from tele_rest.models.edit_general_forum_topic_request import EditGeneralForumTopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditGeneralForumTopicRequest from a JSON string
edit_general_forum_topic_request_instance = EditGeneralForumTopicRequest.from_json(json)
# print the JSON string representation of the object
print(EditGeneralForumTopicRequest.to_json())

# convert the object into a dict
edit_general_forum_topic_request_dict = edit_general_forum_topic_request_instance.to_dict()
# create an instance of EditGeneralForumTopicRequest from a dict
edit_general_forum_topic_request_from_dict = EditGeneralForumTopicRequest.from_dict(edit_general_forum_topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


