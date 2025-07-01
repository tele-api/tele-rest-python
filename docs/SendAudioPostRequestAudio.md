# SendAudioPostRequestAudio

Audio file to send. Pass a file\\_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.send_audio_post_request_audio import SendAudioPostRequestAudio

# TODO update the JSON string below
json = "{}"
# create an instance of SendAudioPostRequestAudio from a JSON string
send_audio_post_request_audio_instance = SendAudioPostRequestAudio.from_json(json)
# print the JSON string representation of the object
print(SendAudioPostRequestAudio.to_json())

# convert the object into a dict
send_audio_post_request_audio_dict = send_audio_post_request_audio_instance.to_dict()
# create an instance of SendAudioPostRequestAudio from a dict
send_audio_post_request_audio_from_dict = SendAudioPostRequestAudio.from_dict(send_audio_post_request_audio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


