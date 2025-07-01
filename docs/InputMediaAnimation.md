# InputMediaAnimation

Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the result, must be *animation* | [default to 'animation']
**media** | **str** | File to send. Pass a file\\_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://\\&lt;file\\_attach\\_name\\&gt;” to upload a new one using multipart/form-data under \\&lt;file\\_attach\\_name\\&gt; name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files) | 
**thumbnail** | **str** | *Optional*. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail&#39;s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can&#39;t be reused and can be only uploaded as a new file, so you can pass “attach://\\&lt;file\\_attach\\_name\\&gt;” if the thumbnail was uploaded using multipart/form-data under \\&lt;file\\_attach\\_name\\&gt;. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files) | [optional] 
**caption** | **str** | *Optional*. Caption of the animation to be sent, 0-1024 characters after entities parsing | [optional] 
**parse_mode** | **str** | *Optional*. Mode for parsing entities in the animation caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**show_caption_above_media** | **bool** | *Optional*. Pass *True*, if the caption must be shown above the message media | [optional] 
**width** | **int** | *Optional*. Animation width | [optional] 
**height** | **int** | *Optional*. Animation height | [optional] 
**duration** | **int** | *Optional*. Animation duration in seconds | [optional] 
**has_spoiler** | **bool** | *Optional*. Pass *True* if the animation needs to be covered with a spoiler animation | [optional] 

## Example

```python
from tele_rest.models.input_media_animation import InputMediaAnimation

# TODO update the JSON string below
json = "{}"
# create an instance of InputMediaAnimation from a JSON string
input_media_animation_instance = InputMediaAnimation.from_json(json)
# print the JSON string representation of the object
print(InputMediaAnimation.to_json())

# convert the object into a dict
input_media_animation_dict = input_media_animation_instance.to_dict()
# create an instance of InputMediaAnimation from a dict
input_media_animation_from_dict = InputMediaAnimation.from_dict(input_media_animation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


