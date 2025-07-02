# EditGeneralForumTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.edit_general_forum_topic_response import EditGeneralForumTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditGeneralForumTopicResponse from a JSON string
edit_general_forum_topic_response_instance = EditGeneralForumTopicResponse.from_json(json)
# print the JSON string representation of the object
print(EditGeneralForumTopicResponse.to_json())

# convert the object into a dict
edit_general_forum_topic_response_dict = edit_general_forum_topic_response_instance.to_dict()
# create an instance of EditGeneralForumTopicResponse from a dict
edit_general_forum_topic_response_from_dict = EditGeneralForumTopicResponse.from_dict(edit_general_forum_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


