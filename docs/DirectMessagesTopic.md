# DirectMessagesTopic

Describes a topic of a direct messages chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic_id** | **int** | Unique identifier of the topic | 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from tele_rest.models.direct_messages_topic import DirectMessagesTopic

# TODO update the JSON string below
json = "{}"
# create an instance of DirectMessagesTopic from a JSON string
direct_messages_topic_instance = DirectMessagesTopic.from_json(json)
# print the JSON string representation of the object
print(DirectMessagesTopic.to_json())

# convert the object into a dict
direct_messages_topic_dict = direct_messages_topic_instance.to_dict()
# create an instance of DirectMessagesTopic from a dict
direct_messages_topic_from_dict = DirectMessagesTopic.from_dict(direct_messages_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


