# SendPollResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_poll_response import SendPollResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendPollResponse from a JSON string
send_poll_response_instance = SendPollResponse.from_json(json)
# print the JSON string representation of the object
print(SendPollResponse.to_json())

# convert the object into a dict
send_poll_response_dict = send_poll_response_instance.to_dict()
# create an instance of SendPollResponse from a dict
send_poll_response_from_dict = SendPollResponse.from_dict(send_poll_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


