# PaidMediaInfo

Describes the paid media added to a message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**star_count** | **int** | The number of Telegram Stars that must be paid to buy access to the media | 
**paid_media** | [**List[PaidMedia]**](PaidMedia.md) | Information about the paid media | 

## Example

```python
from tele_rest.models.paid_media_info import PaidMediaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaidMediaInfo from a JSON string
paid_media_info_instance = PaidMediaInfo.from_json(json)
# print the JSON string representation of the object
print(PaidMediaInfo.to_json())

# convert the object into a dict
paid_media_info_dict = paid_media_info_instance.to_dict()
# create an instance of PaidMediaInfo from a dict
paid_media_info_from_dict = PaidMediaInfo.from_dict(paid_media_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


