# EditMessageReplyMarkupPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message to be edited was sent | [optional] 
**chat_id** | [**EditMessageTextPostRequestChatId**](EditMessageTextPostRequestChatId.md) |  | [optional] 
**message_id** | **int** | Required if *inline\\_message\\_id* is not specified. Identifier of the message to edit | [optional] 
**inline_message_id** | **str** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.edit_message_reply_markup_post_request import EditMessageReplyMarkupPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageReplyMarkupPostRequest from a JSON string
edit_message_reply_markup_post_request_instance = EditMessageReplyMarkupPostRequest.from_json(json)
# print the JSON string representation of the object
print(EditMessageReplyMarkupPostRequest.to_json())

# convert the object into a dict
edit_message_reply_markup_post_request_dict = edit_message_reply_markup_post_request_instance.to_dict()
# create an instance of EditMessageReplyMarkupPostRequest from a dict
edit_message_reply_markup_post_request_from_dict = EditMessageReplyMarkupPostRequest.from_dict(edit_message_reply_markup_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


