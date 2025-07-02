# PostEditMessageReplyMarkupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message to be edited was sent | [optional] 
**chat_id** | [**PostEditMessageTextRequestChatId**](PostEditMessageTextRequestChatId.md) |  | [optional] 
**message_id** | **int** | Required if *inline\\_message\\_id* is not specified. Identifier of the message to edit | [optional] 
**inline_message_id** | **str** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.post_edit_message_reply_markup_request import PostEditMessageReplyMarkupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostEditMessageReplyMarkupRequest from a JSON string
post_edit_message_reply_markup_request_instance = PostEditMessageReplyMarkupRequest.from_json(json)
# print the JSON string representation of the object
print(PostEditMessageReplyMarkupRequest.to_json())

# convert the object into a dict
post_edit_message_reply_markup_request_dict = post_edit_message_reply_markup_request_instance.to_dict()
# create an instance of PostEditMessageReplyMarkupRequest from a dict
post_edit_message_reply_markup_request_from_dict = PostEditMessageReplyMarkupRequest.from_dict(post_edit_message_reply_markup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


