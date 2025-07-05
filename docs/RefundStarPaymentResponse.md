# RefundStarPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.refund_star_payment_response import RefundStarPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RefundStarPaymentResponse from a JSON string
refund_star_payment_response_instance = RefundStarPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(RefundStarPaymentResponse.to_json())

# convert the object into a dict
refund_star_payment_response_dict = refund_star_payment_response_instance.to_dict()
# create an instance of RefundStarPaymentResponse from a dict
refund_star_payment_response_from_dict = RefundStarPaymentResponse.from_dict(refund_star_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


