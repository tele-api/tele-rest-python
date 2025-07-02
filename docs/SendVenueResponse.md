# SendVenueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_venue_response import SendVenueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendVenueResponse from a JSON string
send_venue_response_instance = SendVenueResponse.from_json(json)
# print the JSON string representation of the object
print(SendVenueResponse.to_json())

# convert the object into a dict
send_venue_response_dict = send_venue_response_instance.to_dict()
# create an instance of SendVenueResponse from a dict
send_venue_response_from_dict = SendVenueResponse.from_dict(send_venue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


