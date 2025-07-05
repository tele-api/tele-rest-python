# CloseGeneralForumTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.close_general_forum_topic_response import CloseGeneralForumTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloseGeneralForumTopicResponse from a JSON string
close_general_forum_topic_response_instance = CloseGeneralForumTopicResponse.from_json(json)
# print the JSON string representation of the object
print(CloseGeneralForumTopicResponse.to_json())

# convert the object into a dict
close_general_forum_topic_response_dict = close_general_forum_topic_response_instance.to_dict()
# create an instance of CloseGeneralForumTopicResponse from a dict
close_general_forum_topic_response_from_dict = CloseGeneralForumTopicResponse.from_dict(close_general_forum_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


