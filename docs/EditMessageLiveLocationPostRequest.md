# EditMessageLiveLocationPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message to be edited was sent | [optional] 
**chat_id** | [**EditMessageTextPostRequestChatId**](EditMessageTextPostRequestChatId.md) |  | [optional] 
**message_id** | **int** | Required if *inline\\_message\\_id* is not specified. Identifier of the message to edit | [optional] 
**inline_message_id** | **str** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message | [optional] 
**latitude** | **float** | Latitude of new location | 
**longitude** | **float** | Longitude of new location | 
**live_period** | **int** | New period in seconds during which the location can be updated, starting from the message send date. If 0x7FFFFFFF is specified, then the location can be updated forever. Otherwise, the new value must not exceed the current *live\\_period* by more than a day, and the live location expiration date must remain within the next 90 days. If not specified, then *live\\_period* remains unchanged | [optional] 
**horizontal_accuracy** | **float** | The radius of uncertainty for the location, measured in meters; 0-1500 | [optional] 
**heading** | **int** | Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. | [optional] 
**proximity_alert_radius** | **int** | The maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.edit_message_live_location_post_request import EditMessageLiveLocationPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageLiveLocationPostRequest from a JSON string
edit_message_live_location_post_request_instance = EditMessageLiveLocationPostRequest.from_json(json)
# print the JSON string representation of the object
print(EditMessageLiveLocationPostRequest.to_json())

# convert the object into a dict
edit_message_live_location_post_request_dict = edit_message_live_location_post_request_instance.to_dict()
# create an instance of EditMessageLiveLocationPostRequest from a dict
edit_message_live_location_post_request_from_dict = EditMessageLiveLocationPostRequest.from_dict(edit_message_live_location_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


