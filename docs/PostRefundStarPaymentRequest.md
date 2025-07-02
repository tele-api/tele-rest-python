# PostRefundStarPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Identifier of the user whose payment will be refunded | 
**telegram_payment_charge_id** | **str** | Telegram payment identifier | 

## Example

```python
from tele_rest.models.post_refund_star_payment_request import PostRefundStarPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRefundStarPaymentRequest from a JSON string
post_refund_star_payment_request_instance = PostRefundStarPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(PostRefundStarPaymentRequest.to_json())

# convert the object into a dict
post_refund_star_payment_request_dict = post_refund_star_payment_request_instance.to_dict()
# create an instance of PostRefundStarPaymentRequest from a dict
post_refund_star_payment_request_from_dict = PostRefundStarPaymentRequest.from_dict(post_refund_star_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


