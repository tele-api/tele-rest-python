# ForumTopic

This object represents a forum topic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_thread_id** | **int** | Unique identifier of the forum topic | 
**name** | **str** | Name of the topic | 
**icon_color** | **int** | Color of the topic icon in RGB format | 
**icon_custom_emoji_id** | **str** | *Optional*. Unique identifier of the custom emoji shown as the topic icon | [optional] 

## Example

```python
from tele_rest.models.forum_topic import ForumTopic

# TODO update the JSON string below
json = "{}"
# create an instance of ForumTopic from a JSON string
forum_topic_instance = ForumTopic.from_json(json)
# print the JSON string representation of the object
print(ForumTopic.to_json())

# convert the object into a dict
forum_topic_dict = forum_topic_instance.to_dict()
# create an instance of ForumTopic from a dict
forum_topic_from_dict = ForumTopic.from_dict(forum_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


