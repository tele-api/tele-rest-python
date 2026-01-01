# ForumTopicCreated

This object represents a service message about a new forum topic created in the chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the topic | 
**icon_color** | **int** | Color of the topic icon in RGB format | 
**icon_custom_emoji_id** | **str** | *Optional*. Unique identifier of the custom emoji shown as the topic icon | [optional] 
**is_name_implicit** | **bool** | *Optional*. *True*, if the name of the topic wasn&#39;t specified explicitly by its creator and likely needs to be changed by the bot | [optional] [default to True]

## Example

```python
from tele_rest.models.forum_topic_created import ForumTopicCreated

# TODO update the JSON string below
json = "{}"
# create an instance of ForumTopicCreated from a JSON string
forum_topic_created_instance = ForumTopicCreated.from_json(json)
# print the JSON string representation of the object
print(ForumTopicCreated.to_json())

# convert the object into a dict
forum_topic_created_dict = forum_topic_created_instance.to_dict()
# create an instance of ForumTopicCreated from a dict
forum_topic_created_from_dict = ForumTopicCreated.from_dict(forum_topic_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


