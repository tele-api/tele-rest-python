# HideGeneralForumTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.hide_general_forum_topic_response import HideGeneralForumTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HideGeneralForumTopicResponse from a JSON string
hide_general_forum_topic_response_instance = HideGeneralForumTopicResponse.from_json(json)
# print the JSON string representation of the object
print(HideGeneralForumTopicResponse.to_json())

# convert the object into a dict
hide_general_forum_topic_response_dict = hide_general_forum_topic_response_instance.to_dict()
# create an instance of HideGeneralForumTopicResponse from a dict
hide_general_forum_topic_response_from_dict = HideGeneralForumTopicResponse.from_dict(hide_general_forum_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


