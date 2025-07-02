# PostGetForumTopicIconStickers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[Sticker]**](Sticker.md) |  | 

## Example

```python
from tele_rest.models.post_get_forum_topic_icon_stickers200_response import PostGetForumTopicIconStickers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetForumTopicIconStickers200Response from a JSON string
post_get_forum_topic_icon_stickers200_response_instance = PostGetForumTopicIconStickers200Response.from_json(json)
# print the JSON string representation of the object
print(PostGetForumTopicIconStickers200Response.to_json())

# convert the object into a dict
post_get_forum_topic_icon_stickers200_response_dict = post_get_forum_topic_icon_stickers200_response_instance.to_dict()
# create an instance of PostGetForumTopicIconStickers200Response from a dict
post_get_forum_topic_icon_stickers200_response_from_dict = PostGetForumTopicIconStickers200Response.from_dict(post_get_forum_topic_icon_stickers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


