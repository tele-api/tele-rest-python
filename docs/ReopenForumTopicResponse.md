# ReopenForumTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.reopen_forum_topic_response import ReopenForumTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReopenForumTopicResponse from a JSON string
reopen_forum_topic_response_instance = ReopenForumTopicResponse.from_json(json)
# print the JSON string representation of the object
print(ReopenForumTopicResponse.to_json())

# convert the object into a dict
reopen_forum_topic_response_dict = reopen_forum_topic_response_instance.to_dict()
# create an instance of ReopenForumTopicResponse from a dict
reopen_forum_topic_response_from_dict = ReopenForumTopicResponse.from_dict(reopen_forum_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


