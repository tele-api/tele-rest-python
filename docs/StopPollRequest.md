# StopPollRequest

Request parameters for stopPoll

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message to be edited was sent | [optional] 
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**message_id** | **int** | Identifier of the original message with the poll | 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.stop_poll_request import StopPollRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StopPollRequest from a JSON string
stop_poll_request_instance = StopPollRequest.from_json(json)
# print the JSON string representation of the object
print(StopPollRequest.to_json())

# convert the object into a dict
stop_poll_request_dict = stop_poll_request_instance.to_dict()
# create an instance of StopPollRequest from a dict
stop_poll_request_from_dict = StopPollRequest.from_dict(stop_poll_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


