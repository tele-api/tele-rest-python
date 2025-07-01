# InlineQueryResultLocation

Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the result, must be *location* | [default to 'location']
**id** | **str** | Unique identifier for this result, 1-64 Bytes | 
**latitude** | **float** | Location latitude in degrees | 
**longitude** | **float** | Location longitude in degrees | 
**title** | **str** | Location title | 
**horizontal_accuracy** | **float** | *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500 | [optional] 
**live_period** | **int** | *Optional*. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely. | [optional] 
**heading** | **int** | *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. | [optional] 
**proximity_alert_radius** | **int** | *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**input_message_content** | [**InputMessageContent**](InputMessageContent.md) |  | [optional] 
**thumbnail_url** | **str** | *Optional*. Url of the thumbnail for the result | [optional] 
**thumbnail_width** | **int** | *Optional*. Thumbnail width | [optional] 
**thumbnail_height** | **int** | *Optional*. Thumbnail height | [optional] 

## Example

```python
from tele_rest.models.inline_query_result_location import InlineQueryResultLocation

# TODO update the JSON string below
json = "{}"
# create an instance of InlineQueryResultLocation from a JSON string
inline_query_result_location_instance = InlineQueryResultLocation.from_json(json)
# print the JSON string representation of the object
print(InlineQueryResultLocation.to_json())

# convert the object into a dict
inline_query_result_location_dict = inline_query_result_location_instance.to_dict()
# create an instance of InlineQueryResultLocation from a dict
inline_query_result_location_from_dict = InlineQueryResultLocation.from_dict(inline_query_result_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


