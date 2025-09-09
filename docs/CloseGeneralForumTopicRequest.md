# CloseGeneralForumTopicRequest

Request parameters for closeGeneralForumTopic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberRequestChatId**](RestrictChatMemberRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.close_general_forum_topic_request import CloseGeneralForumTopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloseGeneralForumTopicRequest from a JSON string
close_general_forum_topic_request_instance = CloseGeneralForumTopicRequest.from_json(json)
# print the JSON string representation of the object
print(CloseGeneralForumTopicRequest.to_json())

# convert the object into a dict
close_general_forum_topic_request_dict = close_general_forum_topic_request_instance.to_dict()
# create an instance of CloseGeneralForumTopicRequest from a dict
close_general_forum_topic_request_from_dict = CloseGeneralForumTopicRequest.from_dict(close_general_forum_topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


