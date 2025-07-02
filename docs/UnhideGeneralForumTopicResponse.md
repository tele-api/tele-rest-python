# UnhideGeneralForumTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.unhide_general_forum_topic_response import UnhideGeneralForumTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnhideGeneralForumTopicResponse from a JSON string
unhide_general_forum_topic_response_instance = UnhideGeneralForumTopicResponse.from_json(json)
# print the JSON string representation of the object
print(UnhideGeneralForumTopicResponse.to_json())

# convert the object into a dict
unhide_general_forum_topic_response_dict = unhide_general_forum_topic_response_instance.to_dict()
# create an instance of UnhideGeneralForumTopicResponse from a dict
unhide_general_forum_topic_response_from_dict = UnhideGeneralForumTopicResponse.from_dict(unhide_general_forum_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


