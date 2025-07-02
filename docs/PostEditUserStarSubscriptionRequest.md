# PostEditUserStarSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Identifier of the user whose subscription will be edited | 
**telegram_payment_charge_id** | **str** | Telegram payment identifier for the subscription | 
**is_canceled** | **bool** | Pass *True* to cancel extension of the user subscription; the subscription must be active up to the end of the current subscription period. Pass *False* to allow the user to re-enable a subscription that was previously canceled by the bot. | 

## Example

```python
from tele_rest.models.post_edit_user_star_subscription_request import PostEditUserStarSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostEditUserStarSubscriptionRequest from a JSON string
post_edit_user_star_subscription_request_instance = PostEditUserStarSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(PostEditUserStarSubscriptionRequest.to_json())

# convert the object into a dict
post_edit_user_star_subscription_request_dict = post_edit_user_star_subscription_request_instance.to_dict()
# create an instance of PostEditUserStarSubscriptionRequest from a dict
post_edit_user_star_subscription_request_from_dict = PostEditUserStarSubscriptionRequest.from_dict(post_edit_user_star_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


