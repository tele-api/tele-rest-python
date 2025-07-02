# RefundStarPaymentRequest

Request parameters for refundStarPayment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Identifier of the user whose payment will be refunded | 
**telegram_payment_charge_id** | **str** | Telegram payment identifier | 

## Example

```python
from tele_rest.models.refund_star_payment_request import RefundStarPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefundStarPaymentRequest from a JSON string
refund_star_payment_request_instance = RefundStarPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(RefundStarPaymentRequest.to_json())

# convert the object into a dict
refund_star_payment_request_dict = refund_star_payment_request_instance.to_dict()
# create an instance of RefundStarPaymentRequest from a dict
refund_star_payment_request_from_dict = RefundStarPaymentRequest.from_dict(refund_star_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


