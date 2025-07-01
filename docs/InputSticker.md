# InputSticker

This object describes a sticker to be added to a sticker set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticker** | **str** | The added sticker. Pass a *file\\_id* as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or pass “attach://\\&lt;file\\_attach\\_name\\&gt;” to upload a new file using multipart/form-data under \\&lt;file\\_attach\\_name\\&gt; name. Animated and video stickers can&#39;t be uploaded via HTTP URL. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files) | 
**format** | **str** | Format of the added sticker, must be one of “static” for a **.WEBP** or **.PNG** image, “animated” for a **.TGS** animation, “video” for a **.WEBM** video | 
**emoji_list** | **List[str]** | List of 1-20 emoji associated with the sticker | 
**mask_position** | [**MaskPosition**](MaskPosition.md) |  | [optional] 
**keywords** | **List[str]** | *Optional*. List of 0-20 search keywords for the sticker with total length of up to 64 characters. For “regular” and “custom\\_emoji” stickers only. | [optional] 

## Example

```python
from tele_rest.models.input_sticker import InputSticker

# TODO update the JSON string below
json = "{}"
# create an instance of InputSticker from a JSON string
input_sticker_instance = InputSticker.from_json(json)
# print the JSON string representation of the object
print(InputSticker.to_json())

# convert the object into a dict
input_sticker_dict = input_sticker_instance.to_dict()
# create an instance of InputSticker from a dict
input_sticker_from_dict = InputSticker.from_dict(input_sticker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


