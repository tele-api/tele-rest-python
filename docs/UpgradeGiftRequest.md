# UpgradeGiftRequest

Request parameters for upgradeGift

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**owned_gift_id** | **str** | Unique identifier of the regular gift that should be upgraded to a unique one | 
**keep_original_details** | **bool** | Pass *True* to keep the original gift text, sender and receiver in the upgraded gift | [optional] 
**star_count** | **int** | The amount of Telegram Stars that will be paid for the upgrade from the business account balance. If &#x60;gift.prepaid_upgrade_star_count &gt; 0&#x60;, then pass 0, otherwise, the *can\\_transfer\\_stars* business bot right is required and &#x60;gift.upgrade_star_count&#x60; must be passed. | [optional] 

## Example

```python
from tele_rest.models.upgrade_gift_request import UpgradeGiftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeGiftRequest from a JSON string
upgrade_gift_request_instance = UpgradeGiftRequest.from_json(json)
# print the JSON string representation of the object
print(UpgradeGiftRequest.to_json())

# convert the object into a dict
upgrade_gift_request_dict = upgrade_gift_request_instance.to_dict()
# create an instance of UpgradeGiftRequest from a dict
upgrade_gift_request_from_dict = UpgradeGiftRequest.from_dict(upgrade_gift_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


