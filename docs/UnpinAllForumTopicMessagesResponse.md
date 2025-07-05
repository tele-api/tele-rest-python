# UnpinAllForumTopicMessagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.unpin_all_forum_topic_messages_response import UnpinAllForumTopicMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnpinAllForumTopicMessagesResponse from a JSON string
unpin_all_forum_topic_messages_response_instance = UnpinAllForumTopicMessagesResponse.from_json(json)
# print the JSON string representation of the object
print(UnpinAllForumTopicMessagesResponse.to_json())

# convert the object into a dict
unpin_all_forum_topic_messages_response_dict = unpin_all_forum_topic_messages_response_instance.to_dict()
# create an instance of UnpinAllForumTopicMessagesResponse from a dict
unpin_all_forum_topic_messages_response_from_dict = UnpinAllForumTopicMessagesResponse.from_dict(unpin_all_forum_topic_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


