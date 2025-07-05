# SendVoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_voice_response import SendVoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendVoiceResponse from a JSON string
send_voice_response_instance = SendVoiceResponse.from_json(json)
# print the JSON string representation of the object
print(SendVoiceResponse.to_json())

# convert the object into a dict
send_voice_response_dict = send_voice_response_instance.to_dict()
# create an instance of SendVoiceResponse from a dict
send_voice_response_from_dict = SendVoiceResponse.from_dict(send_voice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


