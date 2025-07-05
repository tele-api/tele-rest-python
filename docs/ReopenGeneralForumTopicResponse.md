# ReopenGeneralForumTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.reopen_general_forum_topic_response import ReopenGeneralForumTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReopenGeneralForumTopicResponse from a JSON string
reopen_general_forum_topic_response_instance = ReopenGeneralForumTopicResponse.from_json(json)
# print the JSON string representation of the object
print(ReopenGeneralForumTopicResponse.to_json())

# convert the object into a dict
reopen_general_forum_topic_response_dict = reopen_general_forum_topic_response_instance.to_dict()
# create an instance of ReopenGeneralForumTopicResponse from a dict
reopen_general_forum_topic_response_from_dict = ReopenGeneralForumTopicResponse.from_dict(reopen_general_forum_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


