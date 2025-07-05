# EditMessageMediaRequest

Request parameters for editMessageMedia

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message to be edited was sent | [optional] 
**chat_id** | [**EditMessageTextRequestChatId**](EditMessageTextRequestChatId.md) |  | [optional] 
**message_id** | **int** | Required if *inline\\_message\\_id* is not specified. Identifier of the message to edit | [optional] 
**inline_message_id** | **str** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message | [optional] 
**media** | [**InputMedia**](InputMedia.md) |  | 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.edit_message_media_request import EditMessageMediaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageMediaRequest from a JSON string
edit_message_media_request_instance = EditMessageMediaRequest.from_json(json)
# print the JSON string representation of the object
print(EditMessageMediaRequest.to_json())

# convert the object into a dict
edit_message_media_request_dict = edit_message_media_request_instance.to_dict()
# create an instance of EditMessageMediaRequest from a dict
edit_message_media_request_from_dict = EditMessageMediaRequest.from_dict(edit_message_media_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


