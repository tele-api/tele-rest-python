# EditForumTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.edit_forum_topic_response import EditForumTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditForumTopicResponse from a JSON string
edit_forum_topic_response_instance = EditForumTopicResponse.from_json(json)
# print the JSON string representation of the object
print(EditForumTopicResponse.to_json())

# convert the object into a dict
edit_forum_topic_response_dict = edit_forum_topic_response_instance.to_dict()
# create an instance of EditForumTopicResponse from a dict
edit_forum_topic_response_from_dict = EditForumTopicResponse.from_dict(edit_forum_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


