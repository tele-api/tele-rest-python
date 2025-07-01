# SendStickerPostRequestSticker

Sticker to send. Pass a file\\_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP sticker from the Internet, or upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files). Video and animated stickers can't be sent via an HTTP URL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.send_sticker_post_request_sticker import SendStickerPostRequestSticker

# TODO update the JSON string below
json = "{}"
# create an instance of SendStickerPostRequestSticker from a JSON string
send_sticker_post_request_sticker_instance = SendStickerPostRequestSticker.from_json(json)
# print the JSON string representation of the object
print(SendStickerPostRequestSticker.to_json())

# convert the object into a dict
send_sticker_post_request_sticker_dict = send_sticker_post_request_sticker_instance.to_dict()
# create an instance of SendStickerPostRequestSticker from a dict
send_sticker_post_request_sticker_from_dict = SendStickerPostRequestSticker.from_dict(send_sticker_post_request_sticker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


