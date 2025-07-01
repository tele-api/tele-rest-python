# CreateForumTopicPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**RestrictChatMemberPostRequestChatId**](RestrictChatMemberPostRequestChatId.md) |  | 
**name** | **str** | Topic name, 1-128 characters | 
**icon_color** | **int** | Color of the topic icon in RGB format. Currently, must be one of 7322096 (0x6FB9F0), 16766590 (0xFFD67E), 13338331 (0xCB86DB), 9367192 (0x8EEE98), 16749490 (0xFF93B2), or 16478047 (0xFB6F5F) | [optional] 
**icon_custom_emoji_id** | **str** | Unique identifier of the custom emoji shown as the topic icon. Use [getForumTopicIconStickers](https://core.telegram.org/bots/api/#getforumtopiciconstickers) to get all allowed custom emoji identifiers. | [optional] 

## Example

```python
from tele_rest.models.create_forum_topic_post_request import CreateForumTopicPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateForumTopicPostRequest from a JSON string
create_forum_topic_post_request_instance = CreateForumTopicPostRequest.from_json(json)
# print the JSON string representation of the object
print(CreateForumTopicPostRequest.to_json())

# convert the object into a dict
create_forum_topic_post_request_dict = create_forum_topic_post_request_instance.to_dict()
# create an instance of CreateForumTopicPostRequest from a dict
create_forum_topic_post_request_from_dict = CreateForumTopicPostRequest.from_dict(create_forum_topic_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


