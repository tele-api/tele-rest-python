# PaidMedia

This object describes paid media. Currently, it can be one of  * [PaidMediaPreview](https://core.telegram.org/bots/api/#paidmediapreview) * [PaidMediaPhoto](https://core.telegram.org/bots/api/#paidmediaphoto) * [PaidMediaVideo](https://core.telegram.org/bots/api/#paidmediavideo)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the paid media, always “video” | [default to 'video']
**width** | **int** | *Optional*. Media width as defined by the sender | [optional] 
**height** | **int** | *Optional*. Media height as defined by the sender | [optional] 
**duration** | **int** | *Optional*. Duration of the media in seconds as defined by the sender | [optional] 
**photo** | [**List[PhotoSize]**](PhotoSize.md) | The photo | 
**video** | [**Video**](Video.md) |  | 

## Example

```python
from tele_rest.models.paid_media import PaidMedia

# TODO update the JSON string below
json = "{}"
# create an instance of PaidMedia from a JSON string
paid_media_instance = PaidMedia.from_json(json)
# print the JSON string representation of the object
print(PaidMedia.to_json())

# convert the object into a dict
paid_media_dict = paid_media_instance.to_dict()
# create an instance of PaidMedia from a dict
paid_media_from_dict = PaidMedia.from_dict(paid_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


