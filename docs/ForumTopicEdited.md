# ForumTopicEdited

This object represents a service message about an edited forum topic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | *Optional*. New name of the topic, if it was edited | [optional] 
**icon_custom_emoji_id** | **str** | *Optional*. New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed | [optional] 

## Example

```python
from tele_rest.models.forum_topic_edited import ForumTopicEdited

# TODO update the JSON string below
json = "{}"
# create an instance of ForumTopicEdited from a JSON string
forum_topic_edited_instance = ForumTopicEdited.from_json(json)
# print the JSON string representation of the object
print(ForumTopicEdited.to_json())

# convert the object into a dict
forum_topic_edited_dict = forum_topic_edited_instance.to_dict()
# create an instance of ForumTopicEdited from a dict
forum_topic_edited_from_dict = ForumTopicEdited.from_dict(forum_topic_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


