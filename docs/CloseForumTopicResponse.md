# CloseForumTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.close_forum_topic_response import CloseForumTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloseForumTopicResponse from a JSON string
close_forum_topic_response_instance = CloseForumTopicResponse.from_json(json)
# print the JSON string representation of the object
print(CloseForumTopicResponse.to_json())

# convert the object into a dict
close_forum_topic_response_dict = close_forum_topic_response_instance.to_dict()
# create an instance of CloseForumTopicResponse from a dict
close_forum_topic_response_from_dict = CloseForumTopicResponse.from_dict(close_forum_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


