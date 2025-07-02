# DeleteForumTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.delete_forum_topic_response import DeleteForumTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteForumTopicResponse from a JSON string
delete_forum_topic_response_instance = DeleteForumTopicResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteForumTopicResponse.to_json())

# convert the object into a dict
delete_forum_topic_response_dict = delete_forum_topic_response_instance.to_dict()
# create an instance of DeleteForumTopicResponse from a dict
delete_forum_topic_response_from_dict = DeleteForumTopicResponse.from_dict(delete_forum_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


