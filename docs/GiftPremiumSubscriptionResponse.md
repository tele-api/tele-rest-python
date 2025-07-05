# GiftPremiumSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.gift_premium_subscription_response import GiftPremiumSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GiftPremiumSubscriptionResponse from a JSON string
gift_premium_subscription_response_instance = GiftPremiumSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(GiftPremiumSubscriptionResponse.to_json())

# convert the object into a dict
gift_premium_subscription_response_dict = gift_premium_subscription_response_instance.to_dict()
# create an instance of GiftPremiumSubscriptionResponse from a dict
gift_premium_subscription_response_from_dict = GiftPremiumSubscriptionResponse.from_dict(gift_premium_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


