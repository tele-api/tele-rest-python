# CreateForumTopicPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**ForumTopic**](ForumTopic.md) |  | 

## Example

```python
from tele_rest.models.create_forum_topic_post200_response import CreateForumTopicPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateForumTopicPost200Response from a JSON string
create_forum_topic_post200_response_instance = CreateForumTopicPost200Response.from_json(json)
# print the JSON string representation of the object
print(CreateForumTopicPost200Response.to_json())

# convert the object into a dict
create_forum_topic_post200_response_dict = create_forum_topic_post200_response_instance.to_dict()
# create an instance of CreateForumTopicPost200Response from a dict
create_forum_topic_post200_response_from_dict = CreateForumTopicPost200Response.from_dict(create_forum_topic_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


