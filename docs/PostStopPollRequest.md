# PostStopPollRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message to be edited was sent | [optional] 
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**message_id** | **int** | Identifier of the original message with the poll | 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.post_stop_poll_request import PostStopPollRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostStopPollRequest from a JSON string
post_stop_poll_request_instance = PostStopPollRequest.from_json(json)
# print the JSON string representation of the object
print(PostStopPollRequest.to_json())

# convert the object into a dict
post_stop_poll_request_dict = post_stop_poll_request_instance.to_dict()
# create an instance of PostStopPollRequest from a dict
post_stop_poll_request_from_dict = PostStopPollRequest.from_dict(post_stop_poll_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


