# UnhideGeneralForumTopicRequest

Request parameters for unhideGeneralForumTopic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberRequestChatId**](RestrictChatMemberRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.unhide_general_forum_topic_request import UnhideGeneralForumTopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnhideGeneralForumTopicRequest from a JSON string
unhide_general_forum_topic_request_instance = UnhideGeneralForumTopicRequest.from_json(json)
# print the JSON string representation of the object
print(UnhideGeneralForumTopicRequest.to_json())

# convert the object into a dict
unhide_general_forum_topic_request_dict = unhide_general_forum_topic_request_instance.to_dict()
# create an instance of UnhideGeneralForumTopicRequest from a dict
unhide_general_forum_topic_request_from_dict = UnhideGeneralForumTopicRequest.from_dict(unhide_general_forum_topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


