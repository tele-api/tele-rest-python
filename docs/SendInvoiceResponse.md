# SendInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_invoice_response import SendInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendInvoiceResponse from a JSON string
send_invoice_response_instance = SendInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(SendInvoiceResponse.to_json())

# convert the object into a dict
send_invoice_response_dict = send_invoice_response_instance.to_dict()
# create an instance of SendInvoiceResponse from a dict
send_invoice_response_from_dict = SendInvoiceResponse.from_dict(send_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


