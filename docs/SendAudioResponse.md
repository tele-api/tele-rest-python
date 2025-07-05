# SendAudioResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_audio_response import SendAudioResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendAudioResponse from a JSON string
send_audio_response_instance = SendAudioResponse.from_json(json)
# print the JSON string representation of the object
print(SendAudioResponse.to_json())

# convert the object into a dict
send_audio_response_dict = send_audio_response_instance.to_dict()
# create an instance of SendAudioResponse from a dict
send_audio_response_from_dict = SendAudioResponse.from_dict(send_audio_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


