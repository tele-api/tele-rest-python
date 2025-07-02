# PostSendVoiceRequestVoice

Audio file to send. Pass a file\\_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_send_voice_request_voice import PostSendVoiceRequestVoice

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendVoiceRequestVoice from a JSON string
post_send_voice_request_voice_instance = PostSendVoiceRequestVoice.from_json(json)
# print the JSON string representation of the object
print(PostSendVoiceRequestVoice.to_json())

# convert the object into a dict
post_send_voice_request_voice_dict = post_send_voice_request_voice_instance.to_dict()
# create an instance of PostSendVoiceRequestVoice from a dict
post_send_voice_request_voice_from_dict = PostSendVoiceRequestVoice.from_dict(post_send_voice_request_voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


