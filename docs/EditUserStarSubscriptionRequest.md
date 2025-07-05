# EditUserStarSubscriptionRequest

Request parameters for editUserStarSubscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Identifier of the user whose subscription will be edited | 
**telegram_payment_charge_id** | **str** | Telegram payment identifier for the subscription | 
**is_canceled** | **bool** | Pass *True* to cancel extension of the user subscription; the subscription must be active up to the end of the current subscription period. Pass *False* to allow the user to re-enable a subscription that was previously canceled by the bot. | 

## Example

```python
from tele_rest.models.edit_user_star_subscription_request import EditUserStarSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditUserStarSubscriptionRequest from a JSON string
edit_user_star_subscription_request_instance = EditUserStarSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(EditUserStarSubscriptionRequest.to_json())

# convert the object into a dict
edit_user_star_subscription_request_dict = edit_user_star_subscription_request_instance.to_dict()
# create an instance of EditUserStarSubscriptionRequest from a dict
edit_user_star_subscription_request_from_dict = EditUserStarSubscriptionRequest.from_dict(edit_user_star_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


