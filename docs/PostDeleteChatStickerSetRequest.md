# PostDeleteChatStickerSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostRestrictChatMemberRequestChatId**](PostRestrictChatMemberRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.post_delete_chat_sticker_set_request import PostDeleteChatStickerSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteChatStickerSetRequest from a JSON string
post_delete_chat_sticker_set_request_instance = PostDeleteChatStickerSetRequest.from_json(json)
# print the JSON string representation of the object
print(PostDeleteChatStickerSetRequest.to_json())

# convert the object into a dict
post_delete_chat_sticker_set_request_dict = post_delete_chat_sticker_set_request_instance.to_dict()
# create an instance of PostDeleteChatStickerSetRequest from a dict
post_delete_chat_sticker_set_request_from_dict = PostDeleteChatStickerSetRequest.from_dict(post_delete_chat_sticker_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


