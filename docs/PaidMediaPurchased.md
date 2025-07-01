# PaidMediaPurchased

This object contains information about a paid media purchase.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**User**](User.md) |  | 
**paid_media_payload** | **str** | Bot-specified paid media payload | 

## Example

```python
from tele_rest.models.paid_media_purchased import PaidMediaPurchased

# TODO update the JSON string below
json = "{}"
# create an instance of PaidMediaPurchased from a JSON string
paid_media_purchased_instance = PaidMediaPurchased.from_json(json)
# print the JSON string representation of the object
print(PaidMediaPurchased.to_json())

# convert the object into a dict
paid_media_purchased_dict = paid_media_purchased_instance.to_dict()
# create an instance of PaidMediaPurchased from a dict
paid_media_purchased_from_dict = PaidMediaPurchased.from_dict(paid_media_purchased_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


