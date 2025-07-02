# StopPollResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Poll**](Poll.md) |  | 

## Example

```python
from tele_rest.models.stop_poll_response import StopPollResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StopPollResponse from a JSON string
stop_poll_response_instance = StopPollResponse.from_json(json)
# print the JSON string representation of the object
print(StopPollResponse.to_json())

# convert the object into a dict
stop_poll_response_dict = stop_poll_response_instance.to_dict()
# create an instance of StopPollResponse from a dict
stop_poll_response_from_dict = StopPollResponse.from_dict(stop_poll_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


