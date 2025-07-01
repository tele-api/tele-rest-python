# PaidMediaPreview

The paid media isn't available before the payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the paid media, always “preview” | [default to 'preview']
**width** | **int** | *Optional*. Media width as defined by the sender | [optional] 
**height** | **int** | *Optional*. Media height as defined by the sender | [optional] 
**duration** | **int** | *Optional*. Duration of the media in seconds as defined by the sender | [optional] 

## Example

```python
from tele_rest.models.paid_media_preview import PaidMediaPreview

# TODO update the JSON string below
json = "{}"
# create an instance of PaidMediaPreview from a JSON string
paid_media_preview_instance = PaidMediaPreview.from_json(json)
# print the JSON string representation of the object
print(PaidMediaPreview.to_json())

# convert the object into a dict
paid_media_preview_dict = paid_media_preview_instance.to_dict()
# create an instance of PaidMediaPreview from a dict
paid_media_preview_from_dict = PaidMediaPreview.from_dict(paid_media_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


