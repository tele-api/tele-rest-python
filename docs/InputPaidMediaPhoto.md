# InputPaidMediaPhoto

The paid media to send is a photo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the media, must be *photo* | [default to 'photo']
**media** | **str** | File to send. Pass a file\\_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://\\&lt;file\\_attach\\_name\\&gt;” to upload a new one using multipart/form-data under \\&lt;file\\_attach\\_name\\&gt; name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files) | 

## Example

```python
from tele_rest.models.input_paid_media_photo import InputPaidMediaPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of InputPaidMediaPhoto from a JSON string
input_paid_media_photo_instance = InputPaidMediaPhoto.from_json(json)
# print the JSON string representation of the object
print(InputPaidMediaPhoto.to_json())

# convert the object into a dict
input_paid_media_photo_dict = input_paid_media_photo_instance.to_dict()
# create an instance of InputPaidMediaPhoto from a dict
input_paid_media_photo_from_dict = InputPaidMediaPhoto.from_dict(input_paid_media_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


