# PostEditMessageTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message to be edited was sent | [optional] 
**chat_id** | [**PostEditMessageTextRequestChatId**](PostEditMessageTextRequestChatId.md) |  | [optional] 
**message_id** | **int** | Required if *inline\\_message\\_id* is not specified. Identifier of the message to edit | [optional] 
**inline_message_id** | **str** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message | [optional] 
**text** | **str** | New text of the message, 1-4096 characters after entities parsing | 
**parse_mode** | **str** | Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**entities** | [**List[MessageEntity]**](MessageEntity.md) | A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse\\_mode* | [optional] 
**link_preview_options** | [**LinkPreviewOptions**](LinkPreviewOptions.md) |  | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.post_edit_message_text_request import PostEditMessageTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostEditMessageTextRequest from a JSON string
post_edit_message_text_request_instance = PostEditMessageTextRequest.from_json(json)
# print the JSON string representation of the object
print(PostEditMessageTextRequest.to_json())

# convert the object into a dict
post_edit_message_text_request_dict = post_edit_message_text_request_instance.to_dict()
# create an instance of PostEditMessageTextRequest from a dict
post_edit_message_text_request_from_dict = PostEditMessageTextRequest.from_dict(post_edit_message_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


