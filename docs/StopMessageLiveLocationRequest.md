# StopMessageLiveLocationRequest

Request parameters for stopMessageLiveLocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message to be edited was sent | [optional] 
**chat_id** | [**EditMessageTextRequestChatId**](EditMessageTextRequestChatId.md) |  | [optional] 
**message_id** | **int** | Required if *inline\\_message\\_id* is not specified. Identifier of the message with live location to stop | [optional] 
**inline_message_id** | **str** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.stop_message_live_location_request import StopMessageLiveLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StopMessageLiveLocationRequest from a JSON string
stop_message_live_location_request_instance = StopMessageLiveLocationRequest.from_json(json)
# print the JSON string representation of the object
print(StopMessageLiveLocationRequest.to_json())

# convert the object into a dict
stop_message_live_location_request_dict = stop_message_live_location_request_instance.to_dict()
# create an instance of StopMessageLiveLocationRequest from a dict
stop_message_live_location_request_from_dict = StopMessageLiveLocationRequest.from_dict(stop_message_live_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


