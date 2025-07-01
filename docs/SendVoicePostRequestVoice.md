# SendVoicePostRequestVoice

Audio file to send. Pass a file\\_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.send_voice_post_request_voice import SendVoicePostRequestVoice

# TODO update the JSON string below
json = "{}"
# create an instance of SendVoicePostRequestVoice from a JSON string
send_voice_post_request_voice_instance = SendVoicePostRequestVoice.from_json(json)
# print the JSON string representation of the object
print(SendVoicePostRequestVoice.to_json())

# convert the object into a dict
send_voice_post_request_voice_dict = send_voice_post_request_voice_instance.to_dict()
# create an instance of SendVoicePostRequestVoice from a dict
send_voice_post_request_voice_from_dict = SendVoicePostRequestVoice.from_dict(send_voice_post_request_voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


