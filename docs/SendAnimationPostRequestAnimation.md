# SendAnimationPostRequestAnimation

Animation to send. Pass a file\\_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.send_animation_post_request_animation import SendAnimationPostRequestAnimation

# TODO update the JSON string below
json = "{}"
# create an instance of SendAnimationPostRequestAnimation from a JSON string
send_animation_post_request_animation_instance = SendAnimationPostRequestAnimation.from_json(json)
# print the JSON string representation of the object
print(SendAnimationPostRequestAnimation.to_json())

# convert the object into a dict
send_animation_post_request_animation_dict = send_animation_post_request_animation_instance.to_dict()
# create an instance of SendAnimationPostRequestAnimation from a dict
send_animation_post_request_animation_from_dict = SendAnimationPostRequestAnimation.from_dict(send_animation_post_request_animation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


