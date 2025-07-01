# PaidMediaPhoto

The paid media is a photo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the paid media, always “photo” | [default to 'photo']
**photo** | [**List[PhotoSize]**](PhotoSize.md) | The photo | 

## Example

```python
from tele_rest.models.paid_media_photo import PaidMediaPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of PaidMediaPhoto from a JSON string
paid_media_photo_instance = PaidMediaPhoto.from_json(json)
# print the JSON string representation of the object
print(PaidMediaPhoto.to_json())

# convert the object into a dict
paid_media_photo_dict = paid_media_photo_instance.to_dict()
# create an instance of PaidMediaPhoto from a dict
paid_media_photo_from_dict = PaidMediaPhoto.from_dict(paid_media_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


