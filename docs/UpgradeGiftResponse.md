# UpgradeGiftResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.upgrade_gift_response import UpgradeGiftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeGiftResponse from a JSON string
upgrade_gift_response_instance = UpgradeGiftResponse.from_json(json)
# print the JSON string representation of the object
print(UpgradeGiftResponse.to_json())

# convert the object into a dict
upgrade_gift_response_dict = upgrade_gift_response_instance.to_dict()
# create an instance of UpgradeGiftResponse from a dict
upgrade_gift_response_from_dict = UpgradeGiftResponse.from_dict(upgrade_gift_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


