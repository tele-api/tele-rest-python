# StopMessageLiveLocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**EditMessageTextResponseResult**](EditMessageTextResponseResult.md) |  | 

## Example

```python
from tele_rest.models.stop_message_live_location_response import StopMessageLiveLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StopMessageLiveLocationResponse from a JSON string
stop_message_live_location_response_instance = StopMessageLiveLocationResponse.from_json(json)
# print the JSON string representation of the object
print(StopMessageLiveLocationResponse.to_json())

# convert the object into a dict
stop_message_live_location_response_dict = stop_message_live_location_response_instance.to_dict()
# create an instance of StopMessageLiveLocationResponse from a dict
stop_message_live_location_response_from_dict = StopMessageLiveLocationResponse.from_dict(stop_message_live_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


