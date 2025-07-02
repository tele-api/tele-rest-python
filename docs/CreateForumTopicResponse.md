# CreateForumTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**ForumTopic**](ForumTopic.md) |  | 

## Example

```python
from tele_rest.models.create_forum_topic_response import CreateForumTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateForumTopicResponse from a JSON string
create_forum_topic_response_instance = CreateForumTopicResponse.from_json(json)
# print the JSON string representation of the object
print(CreateForumTopicResponse.to_json())

# convert the object into a dict
create_forum_topic_response_dict = create_forum_topic_response_instance.to_dict()
# create an instance of CreateForumTopicResponse from a dict
create_forum_topic_response_from_dict = CreateForumTopicResponse.from_dict(create_forum_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


