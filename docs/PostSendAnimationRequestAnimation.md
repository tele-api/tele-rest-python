# PostSendAnimationRequestAnimation

Animation to send. Pass a file\\_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_send_animation_request_animation import PostSendAnimationRequestAnimation

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendAnimationRequestAnimation from a JSON string
post_send_animation_request_animation_instance = PostSendAnimationRequestAnimation.from_json(json)
# print the JSON string representation of the object
print(PostSendAnimationRequestAnimation.to_json())

# convert the object into a dict
post_send_animation_request_animation_dict = post_send_animation_request_animation_instance.to_dict()
# create an instance of PostSendAnimationRequestAnimation from a dict
post_send_animation_request_animation_from_dict = PostSendAnimationRequestAnimation.from_dict(post_send_animation_request_animation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


