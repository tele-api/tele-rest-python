# InputLocationMessageContent

Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of a location message to be sent as the result of an inline query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude of the location in degrees | 
**longitude** | **float** | Longitude of the location in degrees | 
**horizontal_accuracy** | **float** | *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500 | [optional] 
**live_period** | **int** | *Optional*. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely. | [optional] 
**heading** | **int** | *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. | [optional] 
**proximity_alert_radius** | **int** | *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. | [optional] 

## Example

```python
from tele_rest.models.input_location_message_content import InputLocationMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of InputLocationMessageContent from a JSON string
input_location_message_content_instance = InputLocationMessageContent.from_json(json)
# print the JSON string representation of the object
print(InputLocationMessageContent.to_json())

# convert the object into a dict
input_location_message_content_dict = input_location_message_content_instance.to_dict()
# create an instance of InputLocationMessageContent from a dict
input_location_message_content_from_dict = InputLocationMessageContent.from_dict(input_location_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


