# GetForumTopicIconStickersPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[Sticker]**](Sticker.md) |  | 

## Example

```python
from tele_rest.models.get_forum_topic_icon_stickers_post200_response import GetForumTopicIconStickersPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetForumTopicIconStickersPost200Response from a JSON string
get_forum_topic_icon_stickers_post200_response_instance = GetForumTopicIconStickersPost200Response.from_json(json)
# print the JSON string representation of the object
print(GetForumTopicIconStickersPost200Response.to_json())

# convert the object into a dict
get_forum_topic_icon_stickers_post200_response_dict = get_forum_topic_icon_stickers_post200_response_instance.to_dict()
# create an instance of GetForumTopicIconStickersPost200Response from a dict
get_forum_topic_icon_stickers_post200_response_from_dict = GetForumTopicIconStickersPost200Response.from_dict(get_forum_topic_icon_stickers_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


