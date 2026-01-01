# UnpinAllGeneralForumTopicMessagesRequest

Request parameters for unpinAllGeneralForumTopicMessages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberRequestChatId**](RestrictChatMemberRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.unpin_all_general_forum_topic_messages_request import UnpinAllGeneralForumTopicMessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnpinAllGeneralForumTopicMessagesRequest from a JSON string
unpin_all_general_forum_topic_messages_request_instance = UnpinAllGeneralForumTopicMessagesRequest.from_json(json)
# print the JSON string representation of the object
print(UnpinAllGeneralForumTopicMessagesRequest.to_json())

# convert the object into a dict
unpin_all_general_forum_topic_messages_request_dict = unpin_all_general_forum_topic_messages_request_instance.to_dict()
# create an instance of UnpinAllGeneralForumTopicMessagesRequest from a dict
unpin_all_general_forum_topic_messages_request_from_dict = UnpinAllGeneralForumTopicMessagesRequest.from_dict(unpin_all_general_forum_topic_messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


