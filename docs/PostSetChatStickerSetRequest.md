# PostSetChatStickerSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostRestrictChatMemberRequestChatId**](PostRestrictChatMemberRequestChatId.md) |  | 
**sticker_set_name** | **str** | Name of the sticker set to be set as the group sticker set | 

## Example

```python
from tele_rest.models.post_set_chat_sticker_set_request import PostSetChatStickerSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetChatStickerSetRequest from a JSON string
post_set_chat_sticker_set_request_instance = PostSetChatStickerSetRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetChatStickerSetRequest.to_json())

# convert the object into a dict
post_set_chat_sticker_set_request_dict = post_set_chat_sticker_set_request_instance.to_dict()
# create an instance of PostSetChatStickerSetRequest from a dict
post_set_chat_sticker_set_request_from_dict = PostSetChatStickerSetRequest.from_dict(post_set_chat_sticker_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


